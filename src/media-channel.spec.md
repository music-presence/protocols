# Media Channel Protocol

|Date|State|
|-|-|
|2024/11/06|Draft|

## Glossary

**Protocol** - The protocol described in this document.  
**Hub** - The "Music Presence" desktop application.  
**Application** - Any other application running on a desktop computer.  
**Media** - Digital media including music and videos.
that is played back by an Application.  
**Media Metadata** - Information describing and identifying the media,
e.g. media title, artist and album.  
**Media Source** - A source of Media,
such as an Application, a plugin in an Application or a browser extension.  
**Native API** - An operating-system-specific, natively supported API
that supplies Media Metadata about Media that is being played by an Application
and that is usually consumed by the Hub to get information about playing media.
This would be e.g. SMTC on Windows 10 and later,
MediaRemote on macOS 11 and later
and MPRIS on Linux devices.  

## Abstract

The Media Channel protocol is a communication protocol between
any Application and the Hub application
which are both running on the same device.
It is an offline protocol,
meaning that communication only takes place on the device,
protocol messages never leave the device.
The protocol is also connection-oriented,
Applications connect to the Hub,
stay connected to exchange messages,
then disconnect once communication has completed.

The purpose of this protocol is for Applications
to be able to easily communicate to the Hub information
about currently playing Media within the Application,
with an emphasis on music.
More specifically, Applications are expected to always keep the Hub up-to-date
about Media that the Application is playing
for the duration the Application is connected to the Hub,
including some or all relevant Media Metadata.
The protocol is designed to lower the entry barrier
for integrating other desktop applications with the Hub.

Media Channel protocol messages may be exchanged using any transport protocol.
For maximum compatibility though,
the WebSocket protocol is recommended to be used as a transport
using an HTTP server that runs on a specific port on the device
that the Application and the Hub are running on.
In that scenario the Hub is application that exposes the server on that port
and Applications open connections to that port.

## Message format

Protocol messages must be formatted as JSON.

This format is universally accessible in almost all application contexts,
e.g. browsers and desktop applications,
and can be populated easily with very little code,
yet it is complex enough to convey rich information about Media Metadata.

## Identifying the connected Application

## Identifying the Media Source

The source of Media must be uniquely identifiable
within and outside of the Protocol.
The Hub must provide 

For this purpose Media Metadata must always have a `source` field
which must be set to a value that can be associated
with a known Media Source by the Hub.



For this purpose each media source identifier must be:

- either a Root Domain string in Reverse Domain Name Notation, or
- an arbitrary alphanumeric string that may also contain dashes (`-`).

### Matching Protocol Media Metadata with Native API counterparts

## Use Cases

### UC01 - Browser extension to report media from browsers

Browsers can play all types of media from various websites.
Most if not all Native APIs do not report the website
from which the media stems,
making it impossible to discern the real source of the media.

A browser extension can be used to detect the real source of the media
by detecting the domain of the website it is playing on
and then report separate media for each website.

This requires some way of associating Media Metadata with some kind of "source",
which should be the website domain or URL in this scenario.

### UC02 - Reporting Media Metadata that cannot be reported natively

Each Native API has its own set of limitations
regarding metadata that can and cannot be reported.
The Media Channel Protocol can be used
to augment the data that is reported via any such API,
i.e. to add additional metadata to it
that couldn't otherwise be reported to the Hub application.

One such example are WebP album cover images on Windows.
The Windows API does not support this image type [citation needed]
and simply reports no image information at all for WebP type of images.

The Application could use the Media Channel Protocol
to report that image data to the Hub
and the Hub application could then associate that data
with the rest of the metadata that is reported via one of the Native APIs.

This requires some way to match/associate natively reported Media Metadata
with Media Metadata that is reported using the Media Channel Protocol.

### UC03 - Reporting Media Metadata without any Native APIs

Each operating system has its own Native API.
It can be simply too much work to implement each Native API into an Application
when the only goal is to integrate with the Hub application.

For this purpose the Media Channel Protocol could be used
to fully replace Native APIs and take on the job
of reporting Media Metadata about playing media from Applications
to the Hub application.

This requires the Media Channel Protocol to report sufficient metadata
so that it can replace any of the available Native APIs.
