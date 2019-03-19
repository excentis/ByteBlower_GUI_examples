"""
    Lists all scenarios in a ByteBlower GUI project. 
    Useful for scripting tests.

    Expects a single argument: project to parse 
    The names of the scenarios are printed to stdout.
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

for sc in tree.iterfind('Scenario'):
    print(sc.attrib['name'])
