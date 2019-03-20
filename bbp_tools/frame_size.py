"""
    A small tool to resize all Frames in a ByteBlower GUI project.
"""
import sys
import lxml.etree as ET
import random

if len(sys.argv) != 4:
    print('Expected 2 arguments: <src bbp> <target bpp> <new frame size>') 
    sys.exit(-1)

filename = sys.argv[1]
target_name = sys.argv[2]
try:
    new_size = int(sys.argv[3])
except:
    print('The new frame size should be an integer, not "%s"'% sys.argv[3])

try:
    with open(filename, 'r') as f:
        tree = ET.parse(f)
except:
    print("Can't parse '%s'" % filename)

def resize_string(in_str, target_size, filler_char='a'):
    """
        Resizes a string to its new size.       
    """
    new_string = in_str[:target_size]
    new_string += filler_char * (target_size - len(new_string))

    return new_string


for fr in tree.iterfind('Frame'):
    data = fr.attrib['bytesHexString']
    fr.attrib['bytesHexString'] = resize_string(data, 2 * new_size)

tree.write(target_name) 
