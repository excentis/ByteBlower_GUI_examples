#  FrameBlasting examples

On this directory you'll find the FrameBlasting examples. To use them you'll need 
to redock the ports. 

## Intro: What is FrameBlasting?

FrameBlasting is one of the two traffic generation modes of the ByteBlower. The
basic use case is loading the network with UDP traffic.


## frameblasting_basic.bbp
This project has a couple basic FrameBlasting examples. It sends traffic
between two ByteBlower interfaces.

### Scenario: Ex1. frameblasting
The default FrameBlasting flow. Fairly large UDP packets (1024 bytes) being sent from PORT_1 to PORT_2.

### Scenario: Ex2. udp_port_change
This scenario also send UDP packets. As an example the UDP port has been changed to port 9000

### Scenario: Ex3. frameblasting_IPv6
This example is very similar to the first case, only it uses IPv6. In the Frame
view, you'll note that the Layer3 has been configured to IPV6.

## frameblasting_odd_packets.bbp
