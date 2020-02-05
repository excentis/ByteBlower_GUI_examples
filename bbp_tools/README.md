# Intro
This folder has a couple example tools on how to change ByteBlower GUI project
file without opening the GUI. These tools help you automating your test setup.

The tools are written in Python and use lxml for processing the ByteBlower projects.
They should work both in Python3 and Python 2.7

# Prerequisites

We use [lxml](https://lxml.de/) and [scapy](https://scapy.net) packages for processing the ByteBlower projects. You can install these using following command

`pip install lxml`
`pip install scapy`

Some of the scripts need the ByteBlower-API (mostly redocking). An installer is found on http://setup.byteblower.com


# Overview scripts

## change_port_docking.py

## change_port_ipv4.py

## change_port_mac.py

## change_server.py

## copy_frame.py
With this script you can duplicate your frame inside your project and if needed let the UDP source port and|of destination port increment. The result if saved in your output file.


Usage example: `python copy_frame.py -i myProject.bbp -o LotsOfFrames.bbp -n 100 --sport --dport`

The above command will create a copy of the myProject.bbp file to LotsOfFrames.bbp. In the new project file, it will seek your frame and make 100 copies of that frame. The UDP source port will be incremented as well as the UDP destination port.

Show help: `python copy_frame.py -h`

## frame_size.py

## list_batch.py

## list_scenario.py


