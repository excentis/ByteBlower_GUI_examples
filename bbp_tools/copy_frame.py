"""
    A small tool to duplicate frames
    if activated, you can let increment the udp_srcport and udp_dstport
"""
import sys
import getopt
import lxml.etree as ET
from copy import deepcopy
from scapy.all import *
import binascii


def loadFile(src_file):
    try:
        with open(src_file, 'r') as f:
            tree = ET.parse(f)
    except Exception:
        print("Can't read '%s'. Is this a ByteBlower GUI project?" % src_file)
        sys.exit(-1)
    return tree


def writeFile(tree, target_file):
    tree.write(target_file)


def copyFrame(tree, nr_of_copies, sportincr, dportincr):

    for frame in tree.iterfind('Frame'):
        content = frame.get('bytesHexString')

    contentScapy = Ether(binascii.a2b_hex(content))
    parent = frame.getparent()

    sport = contentScapy[UDP].sport
    dport = contentScapy[UDP].dport

    for i in range(1, nr_of_copies + 1):
        newFrame = deepcopy(frame)
        name = newFrame.get('name') + str(i)
        newFrame.set('name', name)
        if sportincr:
            contentScapy[UDP].sport = sport + i
        if dportincr:
            contentScapy[UDP].dport = dport + i
        newFrame.set('bytesHexString', binascii.hexlify(str(contentScapy)))
        parent.append(newFrame)


def printHelp():
    print("Usage: python copy_frame.py -i <inputfile> -o <outputfile> -n <int> [--sport] [--dport]")
    print(" -i \t input ByteBlower GUI file")
    print(" -o \t output ByteBlower GUI file")
    print(" -n \t number of copies to make")
    print("[optional]")
    print(" --sport \t increment the UDP source port")
    print(" --dport \t increment the UDP destination port")


def main(argv):
    src_file = ''
    dst_file = ''
    nr_of_copies = 0
    sportincr = False
    dportincr = False

    try:
        opts, args = getopt.getopt(argv, "hi:o:n:", ["sport", "dport"])
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            printHelp()
            sys.exit()
        elif opt in ("-i"):
            src_file = arg
        elif opt in ("-o"):
            dst_file = arg
        elif opt in ("-n"):
            nr_of_copies = int(arg)
        elif opt in ("--sport"):
            sportincr = True
        elif opt in ("--dport"):
            dportincr = True
    if src_file == '' or dst_file == '' or nr_of_copies == 0:
        print("Missing arguments")
        printHelp()
        sys.exit(2)

    xmlFile = loadFile(src_file)
    copyFrame(xmlFile, nr_of_copies, sportincr, dportincr)
    writeFile(xmlFile, dst_file)


if '__main__' == __name__:
    main(sys.argv[1:])
