"""
    A small tool to change a ports MAC address.
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


def find_docking(serverAddress, new_docking):
    try:
        import byteblowerll.byteblower as bb
        def find_ids(server, to_search):
            interf = None
            for existing in server.PhysicalInterfacesGet():
                print(existing.NameGet())
                if to_search == existing.NameGet():
                    interf = existing
                    break
            else:
              interf = server.InterfaceGetByName(to_search)
                   
            print(dir(interf))
            try:
                interface_id = interf.GetPhysicalInterface().IdGet()
                port_id = interf.PortIdGet()
                return (interface_id, port_id)
            except Exception as e:
                pass

            try:                
                interface_id = interf.IdGet()
                port_id = -1 
                return (interface_id, port_id)
            except:
                raise Exception("Unknown Interface type")

        a_second = int(1e9)
        api = bb.ByteBlower.InstanceGet()
        server = api.ServerAdd(serverAddress, 9002, a_second)
        return find_ids(server, new_docking)
    except Exception as e:
        print(e)
    # We couldn't ask the ByteBlower Server for the port.
    # Let's take an educated guess.



def change_port_docking(port, new_server_address, new_docking):
    for portConfig in port.iterfind('ByteBlowerGuiPortConfiguration'):
        server_address = new_server_address or portConfig['physicalServerAddress']
        interface_id, port_id = find_docking(server_address, new_docking) 
        portConfig.attrib['physicalInterfaceId'] = str(interface_id)
        portConfig.attrib['physicalPortId'] = str(port_id)
        portConfig.attrib['physicalServerAddress'] = server_address 
       

def write_project(project, new_file):
    project.write(new_file)


def main():
    if 4 <= len(sys.argv)  <= 5:
        print('Expected 4 or 5 arguments:')
        print('     Same ByteBlower Server:       <src bbp> <target bpp> <port name> <new docking>')
        print('     Different ByteBlower Sserver: <src bbp> <target bpp> <port name> <server-address> <new docking>')
        sys.exit(1)

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

    bbp = read_project(filename)
    if bbp is None:
        sys.exit(1)

    port = find_port(bbp, port_name)

    if port is None:
        print("Could not find port '%s' in the project." % port_name)
        sys.exit(1)

    change_port_docking(port, new_server_address, new_docking)

    write_project(bbp, target_name)


if __name__ == '__main__':
    main()
