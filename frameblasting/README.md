#  FrameBlasting examples

On this directory you'll find the FrameBlasting examples. To use them you'll need 
to re-dock the ByteBlower Ports. 

## Intro: What is FrameBlasting?

FrameBlasting is one of the two traffic generation modes of the ByteBlower. The system
offers you precies control over content and transmission speed.

The most common use case is generating UDP traffic. 4 out of the 5 examples will demonstrate 
this. The odd frames example is an exception, check this project out for the other traffic types.

Each of the sections each reference one of the ByteBlower project files. To get started,
* Download and open the file in the ByteBlower GUI.
* Read the associated secion
* Create the setup and rerun the tests.

## <a id="raw-url" href="https://raw.githubusercontent.com/excentis/ByteBlower_GUI_examples/origin/documentation_cleanup/frameblasting/frameblasting_basic.bbp" download="frameblasting_basic.bbp"> frameblasting_basic.bbp </a>
This project has a couple basic FrameBlasting examples. The main goal is to show the essentials
behind FrameBlasting: ByteBlower ports, configuring speed and modifiying the contents of the traffic..

In all cases traffic is generated between 2 ByteBlower Interfaces: trunk-1-1 and trunk-1-2. Just like the 
[quicktest](https://setup.byteblower.com/setup.php?type=5100#using), this project assumes a direct
connection between between both interfaces. Creating this setup the first step to get started. 

### Scenario: Ex1. frameblasting
The default FrameBlasting flow. Fairly large UDP packets (1024 bytes) being sent from PORT_1 to PORT_2.

### Scenario: Ex2. udp_port_change
This scenario also send UDP packets. As an example the UDP port has been changed to port 9000

### Scenario: Ex3. frameblasting_IPv6
This example is very similar to the first case, only it uses IPv6. In the Frame
view, you'll note that the Layer3 has been configured to IPV6.

## Latency.bbp
Frameblasting flows can be used for Latency Measurements. This project shows
a couple use-cases.

* Ex 1. default-latency: The default latency measurement.
* Ex 2. Latency under load: In the same scenario we measure both the base latency and the latency when the network fully loaded (1Gbit/s).
* Ex 3. Latency with TCP: An example of combining both latency measurement with a Tcp flow. 

## NAT.bbp

This project shows a couple tests of a NAT device. 

The project uses 4 ByteBlower ports: one is docked in the WAN, the other 3 are
behind the NAT device. The Port on the WAN side is publicly accessible.
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
Unlike the previous scenarios, this is a negative test: we don't expect any
traffic to through here.

## frameblasting_odd_packets.bbp
In this project we deviate from the standard usecase: instead of nice UDP
traffic we'll challenge the network with purposely wrong traffic.

The project assumes that the ByteBlower ports are docked behind a NAT-device
(or any type of modem or access point). We make this assumption mostly because
such devices are the most sensitive to the generated traffic.

A default, UDP frameblasting flow checks whether we are successful in disrupting the
device under test.

### Ex 1. Syn blasting
This scenario floods the network with TCP-syn packets. The NAT-device should ignore them fairly quickly.

### Ex 2. Wrong checksums
Small packets with purposely wrong IPv4 header checksum and IPv4 length.

### Ex 3. Wrong Ether types
Sends out traffic with an uncommon Ether type (0x500)

### Ex 4. Broadcast traffic
An example how to broadcast UDP traffic. This the most benign of all the
scenarios. The rate is also fairly low (<1 MBit/s).



