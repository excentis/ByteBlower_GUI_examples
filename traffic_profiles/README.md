# Traffic profiles 

This folder contains various traffic profiles implemented in the ByteBlower 
GUI.

## Traffic profile: Browsing
This traffic profile emulates web-browsing. You can implement this very 
easy with the payload based TCP profiles.

### Scenario: Website visit
This scenario visits a website. During this visits several files are
download from a 9 different web servers.

## Traffic profile: Gaming
Emulates a gaming session taking place. During this session there's
a small upstream load with updates from the game client. The gaming
server sends a regular update downstream.

The upstream load is much smaller than the downstream one.


## Traffic profile: Cloud file share
This project demonstrates how to emulate web traffic. It shows a small
requests for e.g.

### Scenario: File Download
Downloads a large file from a webserver. We take a Linux installers as 
the example.

### Scenario: Files upload
Uploads files to a webserver. It shows uploading a small image file and we
show a backup being synchronized with a remote server.


## Traffic profile: Video streaming
In this example you'll find a couple examples on how to emulate a video stream.
It includes 3 quality settings (default, High-Definition and Ultra High Definition).

Of the last UHD profile, the project shows two ways to implement it. We'll briefly
explain both in the paragraphs below.


The first approach uses payload based flows. This approach is closed to the DASH.
In sequence it configures several downloads on an HTTP server. Each download 
represents retrieving part of the video. The video-rate is emulated by changing
the size of the download.

The second approach uses time based TCP flows. In contrast to the first you need
less objects to configure in the ByteBlower GUI. This makes it more flexible.
The downside is that is less realistic. There's no guarantee that the download
retrieves the necessary amount.

Both approaches have a large download at their start. This emulates filling up
the video buffer.

### Scenario Default 
In here we emulate 1.5 Mbit/s video flow. This is about 360p.


### Scenario HD
A 5Mbit/s video flow, close 720p a second.

### Scenario UHD
The last of the first video emulation approach. This scenario emulates a
24Mbit/s video flow, or close to 4K.

### Scenario UHD other approach
In this scenario we use the time based approach to emulate the video traffic.
We need only a single HTTP flow.  This flow is reused multiple times. 
