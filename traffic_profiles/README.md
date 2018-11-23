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
Emulates a gaming session taking place. Durign this session there's
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
In this exmaple you'll find a couple examples on how to emulate a video stream.
It includes 3 quality settings (default, High-Definition and Ultra High Definition).

Of the last UHD profile, the project shows two ways to implement it.

