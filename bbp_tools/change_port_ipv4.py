"""
    A small tool to change a ports Layer3 configuration.
"""
import sys
from lxml import etree


def read_project(project_filename):
    try:
        with open(project_filename, 'r') as f:
            tree = etree.parse(f)
            return tree
    except FileNotFoundError:
        print("Cannot read file '%s'" % project_filename)
    except etree.ParseError:
        print("Can't parse '%s'" % project_filename)
    return None


def find_port(project, port_name):
    for port in project.iterfind("ByteBlowerGuiPort"):
        if port.attrib['name'] == port_name:
            return port
    return None


def _set_address(obj, new_address):
    address_list = new_address.split('.')

    for i in range(4):
        new_val = int(address_list[i])
        if new_val > 127:
            new_val = (256 - new_val) * -1

        obj[i].text = str(new_val)


def set_port_fixed(port, ip, netmask, gateway):
    for l3config in port.iterfind("ipv4Configuration"):
        l3config.attrib['addressConfiguration'] = "Fixed"

        for ip_obj in l3config.iterfind("IpAddress"):
            _set_address(ip_obj, ip)

        for netmask_obj in l3config.iterfind("Netmask"):
            _set_address(netmask_obj, netmask)

        for gateway_obj in l3config.iterfind("DefaultGateway"):
            _set_address(gateway_obj, gateway)


def write_project(project, new_file):
    project.write(new_file)


def main():
    if len(sys.argv) != 7:
        print("Syntax: {} <src_bbp> <target bbp> <port_name> <ip address> <netmask> <gateway>".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]
    target_name = sys.argv[2]

    port_name = sys.argv[3]

    ip = sys.argv[4]
    netmask = sys.argv[5]
    gateway = sys.argv[6]

    bbp = read_project(filename)
    if bbp is None:
        sys.exit(1)

    port = find_port(bbp, port_name)

    if port is None:
        print("Could not find port '%s'" % port_name)
        sys.exit(1)

    set_port_fixed(port, ip, netmask, gateway)

    write_project(bbp, target_name)


if __name__ == '__main__':
    main()
