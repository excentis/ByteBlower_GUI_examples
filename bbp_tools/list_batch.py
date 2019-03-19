"""
    A simple tool to list all batches in a ByteBlower Project.
    This list is printed to standard output.
"""
import sys 
import lxml.etree as ET

if len(sys.argv) != 2:
    print('Expected 1 argument: ByteBlower GUI project to parse')
    sys.exit(-1)

filename = sys.argv[1]
try:
    with open(filename, 'r') as f:
        tree = ET.parse(f)
except:
    print("Can't parse '%s'" % filename)

for sc in tree.iterfind('Batch'):
    print(sc.attrib['name'])
