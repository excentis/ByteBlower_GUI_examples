"""
    A small tool to change the address of the ByteBlower server
    in a project.
"""
import sys
import lxml.etree as ET

if len(sys.argv) != 4:
    print('Expected 3 arguments: <src project> <target project> <new address>')
    sys.exit(-1)

src_file = sys.argv[1]
target_file = sys.argv[2]
new_server_address = sys.argv[3]

try:
    with open(src_file, 'r') as f:
        tree = ET.parse(f)
except:
    print("Can't read '%s'. Is this a ByteBlower GUI project?" % src_file)

for port in tree.iterfind('ByteBlowerGuiPort'):
    for config in port.iterfind('ByteBlowerGuiPortConfiguration'):
        config.attrib['physicalServerAddress'] = new_server_address

tree.write(target_file)    
