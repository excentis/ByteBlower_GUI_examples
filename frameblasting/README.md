#  FrameBlasting examples

On this directory you'll find the FrameBlasting examples. To use them you'll need 
to redock the ports. 

## Intro: What is FrameBlasting?

FrameBlasting is one of the two traffic generation modes of the ByteBlower. The
basic use case is loading the network with UDP traffic.


## frameblasting_basic.bbp
This project has a couple basic FrameBlasting examples. It sends traffic
between two ByteBlower interfaces. 

It shows the basic use-case of (slightly) loading the network with UDP 
traffic. 

A good first step after this example is to increase the speed of the flows
drastically. Since 2.9.0, most models should easily be able to sent these
frames at line-rate.

### Scenario: Ex1. frameblasting
The default FrameBlasting flow. Fairly large UDP packets (1024 bytes) being sent from PORT_1 to PORT_2.

### Scenario: Ex2. udp_port_change
This scenario also send UDP packets. As an example the UDP port has been changed to port 9000

### Scenario: Ex3. frameblasting_IPv6
This example is very similar to the first case, only it uses IPv6. In the Frame
view, you'll note that the Layer3 has been configured to IPV6.

## frameblasting_odd_packets.bbp
In this project we deviate from the standard usecase: instead of nice UDP
traffic we'll challenge the network with purposely wrong traffic.

The project assumes that the ByteBlower ports are docked behind a NAT-device
(or any type of modem or access point). We make this assumption mostly because
such devices are the most senstive to the generated traffic.

A default, UDP frameblasting flow checks whether we are successful in disrupting the
device under test.

### Ex 1. Syn blasting
This scenario floods the netwerk with TCP-syn packets. The NAT-device should ignore them fairly quickly.

### Ex 2. Wrong checksums
Small packets with purposely wrong IPv4 header checksum and IPv4 length.

### Ex 3. Wrong Ether types
Sends out traffic with an uncommon Ether type (0x500)

### Ex 4. Broadcast traffic
An example how to broadcast UDP traffic. This the most benign of all the
scenarios. The rate is also fairly low (<1 MBit/s).


## NAT.bbp

This project shows a couple tests of a NAT device. 

The project uses 4 ByteBlower ports: one is docked in the WAN, the other 3 are
behind the NAT device. The Port on the WAN side is publicly acessible.
You'll notice that even though all ByteBlower ports are behind the NAT, we've only
enabled the NAT flag on two of them.


### Scenario: Ex1. Basic Nat
The default config to test a device behind a NAT. In this case we'll send traffic
downstream: from the WAN to inside the LAN. 

In practice, many devices will uses the same UDP port number for the private
(inside the NAT) and the public (WAN-side).

### Scenario: Ex2. Force remap
A slightly more complex scenario. We send traffic to two different ByteBlower
Ports inside the LAN. To the outside world (the WAN) both ByteBower ports have
the same public IP address.

Unlike the first scenario, the NAT can't do an identity mapping for both.

### Scenario: Ex3. NAT timeout check
A simple scenario to check the timeout of the NAT entry. The setup is the same
as the first scenario, but the duration is much longer.

### Scenario: Ex4. Blocked traffic
Unlike the previous scenarios, this is a negative test: we don't expect any traffic to through here.
