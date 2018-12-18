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

Creating a FrameBlasting based throughput measurement. Starts first with
choosing the packet size. Large packets (1500 bytes) tend to load the mostly
the network, while with smaller sizes you can search for packet-processing
bottlenecks. You can also mix different packet sizes to make the test more
realistic.

After the picking packet sizes, you'll need to estimate the bandwidth of the
setup. The load configured for the FrameBlasting flow should be higher then
your expectation.  An easy guess is choosing 10 Gbit/s, but it helps to be
closer to the actual value.  It's not unusual for the device under test to
crash and reboot when strained way beyond normal operation.

### Good:
* Easy to debug.
* Easily control all parameters.

### Bad:
* Overloading the system too much makes the results variable.
* Can be become repitive when trying to pick the best estimate inital estimate. 
* Requires some inital setup work.


## RFC-2544 based throughput measurement

