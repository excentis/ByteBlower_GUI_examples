"""
    A small tool to change a ports MAC address.
"""
import sys
from lxml import etree


class ProjectParseError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class PortNotFound(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class AutoCleanupMeetingPoint(object):
    """ Contextmanager which automatically removes the meetingpoint when the object goes out of scope
        :param address: The address on which the ByteBlower MeetingPoint is reachable
        :type address: str
        :param port: The TCP port number on which the server listens.  9101 is the default
        :type port: int
        :param timeout: Number of nanoseconds to wait for the server to respond
        :type timeout: int
        :return: A server object
        :rtype: :class:`byteblowerll.byteblower.ByteBlowerServer`

    """

    def __init__(self, address, port=9101, timeout=int(1e9)):
        self._address = address
        self._meetingpoint = None
        self._port = port
        self._timeout = timeout

    def __enter__(self):
        from byteblowerll import byteblower
        instance = byteblower.ByteBlower.InstanceGet()
        self._meetingpoint = instance.MeetingPointAdd(self._address, self._port, self._timeout)
        return self._meetingpoint

    def __exit__(self, *args, **kwargs):
        from byteblowerll import byteblower
        instance = byteblower.ByteBlower.InstanceGet()
        try:
            instance.MeetingPointRemove(self._meetingpoint)
        except byteblower.ByteBlowerAPIException:
            pass
        self._meetingpoint = None


class ByteBlowerProjectFile(object):
    """Simple class representing a ByteBlower project file"""

    def __init__(self, filename):
        self._filename = filename
        self._tree = None

    def load(self):
        """ Reads the file from disk and parses it
        :raises: :class:`.ProjectParseError` when the project could not be parsed
        :raises: :class:`FileNotFoundException` when the project cannot be found
        """
        try:
            with open(self._filename, 'r') as f:
                self._tree = etree.parse(f)

                if self._tree is None:
                    raise ProjectParseError("Can't parse '%s'" % self._filename)
        except etree.ParseError:
            raise ProjectParseError("Can't parse '%s'" % self._filename)

    def save(self):
        self.save_as(self._filename)

    def save_as(self, new_filename):
        self._tree.write(new_filename)

    def get_port_docking(self, port_name):
        """Gets the current port docking information
        :return: The current docking information (server_address, physical_interface_id, byteblower_interface_id)
        :rtype: tuple
        """
        port = self._find_port(port_name)

        for portConfig in port.iterfind('ByteBlowerGuiPortConfiguration'):
            attributes = portConfig.attrib

            return (
                attributes['physicalServerAddress'],
                attributes['physicalInterfaceId'],
                attributes['physicalPortId']
            )

        return None

    def update_port_docking(self, port_name, server_address, endpoint_uuid):
        port = self._find_port(port_name)

        for portConfig in port.iterfind('ByteBlowerGuiPortConfiguration'):
            attributes = portConfig.attrib
            new_server_address = server_address or attributes['physicalServerAddress']

            attributes['physicalInterfaceId'] = endpoint_uuid
            attributes['physicalServerType'] = 'MeetingPoint'
            attributes['physicalServerAddress'] = new_server_address

    def _find_port(self, port_name):
        for port in self._tree.iterfind("ByteBlowerGuiPort"):
            if port.attrib['name'] == port_name:
                return port

        raise PortNotFound("Could not find a port named '{}' in project '{}'".format(port_name, self._filename))


def _guess_docking_parameters(endpoint_name):
    # type: (str) -> str
    print("Warning: Guessing interface '%s' docking parameters" % endpoint_name)

    return endpoint_name


def _get_docking_parameters_from_server(server_address, endpoint_name):
    # type: (str, str) -> str
    try:
        from byteblowerll import byteblower
    except ImportError:
        # Aargh, no API available, we can't do our job!
        print("Warning: could not find the ByteBlower API")
        return None

    connect_timeout_ns = int(1e9)  # one second

    try:
        with AutoCleanupMeetingPoint(server_address, timeout=connect_timeout_ns) as meetingpoint:  # type: byteblower.MeetingPoint
            for endpoint in meetingpoint.DeviceListGet():
                assert isinstance(endpoint, byteblower.WirelessEndpoint)
                device_info = endpoint.DeviceInfoGet()

                if endpoint_name not in [device_info.GivenNameGet(), endpoint.DeviceIdentifierGet()]:
                    continue

                device_status = endpoint.StatusGet()
                if device_status == byteblower.DeviceStatus.Unavailable:
                    print("Warning: Endpoint is not available!")
                elif device_status == byteblower.DeviceStatus.Running:
                    print("Warning: Endpoint already running a test!")

                return endpoint.DeviceIdentifierGet()

    except byteblower.ConfigError as e:
        print("Warning: An error occurred while querying", e.what())
        return None

    except byteblower.ByteBlowerAPIException as e:
        print("Warning: could not connect to the ByteBlower MeetingPoint", e.what())
        return None

    print("Warning: Unknown device", endpoint_name)
    return None


def find_docking_parameters(server_address, new_docking):
    # type: (str, str) -> str
    _docking_params = _get_docking_parameters_from_server(server_address, new_docking)

    if _docking_params is not None:
        # it worked, return those
        return _docking_params

    # We couldn't ask the ByteBlower Server for the port.
    # Let's take an educated guess.
    return _guess_docking_parameters(new_docking)


def main():
    if not (5 <= len(sys.argv) <= 6):
        print('Expected 4 or 5 arguments:')
        print('     Same ByteBlower MeetingPoint:      <src bbp> <target bpp> <port name> <endpoint-name>')
        print('     Same ByteBlower MeetingPoint:      <src bbp> <target bpp> <port name> <endpoint-uuid>')
        print('     Different ByteBlower MeetingPoint: <src bbp> <target bpp> <port name> <meetingpoint-address> <endpoint-name>')
        print('     Different ByteBlower MeetingPoint: <src bbp> <target bpp> <port name> <meetingpoint-address> <endpoint-uuid>')
        return 1

    arguments = sys.argv[:]
    # Just add the server, avoid
    # making it a special case.
    if len(arguments) == 5:
        arguments.insert(4, None)

    filename = arguments[1]
    target_name = arguments[2]

    port_name = arguments[3]
    new_server_address = arguments[4]
    new_docking = arguments[5]

    try:
        project = ByteBlowerProjectFile(filename)
        project.load()

        if new_server_address is None:
            # no server address given,
            # we need to get the current docking parameters to get the last docked server.

            current_docking_params = project.get_port_docking(port_name)

            if current_docking_params is None:
                print("Error: No server address given and the port was never docked to a server before.")
                return 1

            new_server_address, _, _ = current_docking_params

        docking_parameters = find_docking_parameters(new_server_address, new_docking)

        if docking_parameters is None:
            # something went wrong
            return 1

        project.update_port_docking(port_name, new_server_address, endpoint_uuid=docking_parameters)

        project.save_as(target_name)

    except FileNotFoundError:
        print("Could not read project '%s'" % filename)
        return 1

    except Exception as e:
        print(str(e))
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
