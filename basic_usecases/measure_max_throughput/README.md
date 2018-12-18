# Measuring the maximum throughput of your modem.

A common question is measuring the maximum throughput of your system.
We'll focus here on doing the measurement, not on where the bottleneck lies.

With your ByteBlower, there are 3 approaches to measure the throughput of your modem. Each has it's own use-case.

* 1. Measure the throughput based on a TCP flow.
* 2. Load the modem with a FrameBlasting flow.
* 3. Use the RFC-2544 throughput test.


## TCP-based measurement.
This approach is the easiest of them all. TCP by design limits itself to the
available bandwidth. The final throughput of your TCP flow is thus decent
estimate of how fast users can go.

To set it up, you'll only need to configure a TCP flow. You tweak the TCP
settings in the TCP view, but at this point it's probably better to look at the
other apporaches below. The sole expection is perhaps the receive window, this
value should be as high as possible: start from 8.

### Good:
* Easy to set up.
* Close to user experience.


### Bad:
* Result can vary significantly, especially when one part in the system isn't mishaving.
* Not easy measuring speed at different packet sizes.
* Sends traffic in both up- and downstream.



## UDP-frameblasting approach
The second approach goes into a wholly different direction. We wont try to
limit the rate we're sending out packets, our only interest is the amount of
received data. This approach requires a bit of work to set it up, but pays
itself off down the road.

Creating a FrameBlasting based throughput measurement starts with choosing the
packet size. Large packets (1500 bytes) tend to load the mostly the network,
while with smaller sizes you can search for packet-processing bottlenecks. You
can also mix different packet sizes to make the test more realistic.

After the picking packet sizes, you'll need to estimate the bandwidth of the
setup. The load configured for the FrameBlasting flow should be higher then the
availabel bandwidth. An easy guess is choosing 10 Gbit/s, but it helps to be
closer to the actual value. Straining systems way beyond their limits makes the
results unreliable, it's not even unusual for devices to crash during the test.

### Good:
* Easily to control, Easy to debug.
* Gets results quickly.

### Bad:
* Results vary on how close your initial estimate is, it Can be become repitive when trying to pick the best one. 
* Requires inital setup work.


## RFC-2544 based throughput measurement
Just like the previous approach you'll use FrameBalsting to load the system. A
major improvement is that you'll let the ByteBlower GUI doing the guessing.
This removes much of your workload, increases precission of the result but also
results in a longer test duration.

Configuring this test is done with the RFC-2544 wizard. In addition to the 
chosing frame size, you can also configure how much loss you can affort to 
sustain and how long the system should try each bandwidth


### Good:
* Reliable, controllable results for each setup.


### Bad:
* Long test time.
* Requires some thougth on configuration parameters.


