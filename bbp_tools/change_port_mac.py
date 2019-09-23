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


def change_port_mac(port, new_mac):
    mac_list = []
    if ':' in new_mac:
        mac_list = new_mac.split(':')
    else:
        print("Unknown mac address format.  Please provide the mac as 00:11:22:33:44:55")
        sys.exit(1)

    for l2 in port.iterfind('layer2Configuration'):
        for macaddress in l2.iterfind('MacAddress'):
            for i in range(6):
                new_val = int(mac_list[i], 16)
                if new_val > 127:
                    new_val = (256 - new_val) * -1

                macaddress[i].text = str(new_val)


def write_project(project, new_file):
    project.write(new_file)


def main():
    if len(sys.argv) != 5:
        print('Expected 4 arguments: <src bbp> <target bpp> <port name> <new mac address>')
        sys.exit(1)

    filename = sys.argv[1]
    target_name = sys.argv[2]

    port_name = sys.argv[3]
    new_mac = sys.argv[4]

    bbp = read_project(filename)
    if bbp is None:
        sys.exit(1)

    port = find_port(bbp, port_name)

    if port is None:
        print("Could not find port '%s'" % port_name)
        sys.exit(1)

    change_port_mac(port, new_mac)

    write_project(bbp, target_name)


if __name__ == '__main__':
    main()
