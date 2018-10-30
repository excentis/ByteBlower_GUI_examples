# TCP examples 

The ByteBlower has a fully functional TCP implementation. It allows you to
configure essential TCP options.

In this folder you'll find the TCP examples. They start at a bit higher level
than the frameblasting ones.  If you're new to the ByteBlower GUI, it's best to
first begin with those.

## TCP.bbp

### Scenario: Ex 1. Rate limit 60Mbit
A TCP flow with a ratelimit of 60 Mbit. This ratelimit is part of the TCP
template. You'll configure it on the TCP view.

### Scenario: Ex2: TCP serveral window scales
This scenario has 3 flows. Each flow has a slightly different TCP
configuration, the windowscale is configured to 0, 1 (times 2), 8 (times 256).
To show the effect of these values, there's no overlap between the flows.

If there's suffucient bandwidth available, you'll notice that:
* The flow with windows scale 1 is almost twice as fast compared to the window scale 0.
* Only the flow with window scale 8 fills the whole capacity of the line.

### Scenario: Ex3. Slow starting TCP flow


### Scenario: Ex4a. Compoeting window scales

### Scenario: Ex4b. Compoeting Congestion algortihms

### Scenario: Ex4c. Competing start time
