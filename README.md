#HTTP/2 Frame Visualizer

## Project Overview

The web is moving to a new HTTP protocol, HTTP/2.

This is a tool for visualizing the frames of an HTTP/2 request/response stream in
real time. HTTP/1.x, the previous standard still in widespread use today, passes
a continuous stream of text (always beginning with a precisely-formatted header) back and forth with
every new request and response. Under the old spec, it's possible to build a
simple HTTP server from scratch using a simple TCP socket interface. If you're building your
own HTTP/1.x client, just send a properly formatted request and you'll get a well-formatted header and text field in response.  It's a great exercise,
and you can see my implementation of a simple HTTP/1.1 server here. You can also approximate
a simple curl request on the command line.  Just type

`curl -v http://(any site)`

and you're seeing everything transmitted over the HTTP protocal (including
the coordinating headers) exactly as your browser would.

But the new HTTP/2 spec makes the process a lot less straightforward and transparent (not to mention potentially harder to debug!).  Both requests and responses are broken up into
frames, a slice of the HTTP
request and response with defined parameters. For example, there are DATA frames, PRIORITY frames, SETTINGS frames, PUSH PROMISE frames, and others that help coordinate both aspects of the HTTP protocol that are familiar from HTTP/1.1 and HTTP/2's new features.  You can find a full list of HTTP/2 frames at the [official spec](https://tools.ietf.org/html/rfc7540#section-6).

## Goals

The dev tools for a modern browser like Chrome already translate HTTP/2 requests and responses back
into old-style HTTP/1.1 headers.  To see this for yourself, visit Chrome's
"Network" tab and go to [Twitter](www.twitter.com), a site that offers the HTTP/2 spec
for compatible browsers. Click on any request or response that uses the
"h2"(HTTP/2) protocol and it will show you headers in the old HTTP/1.1 style.
The frames are hidden, but that doesn't mean they are not there!  With HTTP/2,
we've added a layer of complexity to the HTTP spec that is hidden from our dev
tools and from developers, which is sure to cause problems down the line as the
HTTP/2 spec is integrated into more frameworks and becomes a daily part of life
for many developers. Without a bit of knowledge about the underlying mechanics
of HTTP/2, a developer could be unaware that the basic protocol of the web has
shifted to this new object called a "frame!"

This project is aimed at a developer audience, along with anyone else interested
in web technologies.  It builds a basic toolkit of visualizations that helps demystify the inner workings of HTTP/2.
 
## Technical Components

* Visualizations constructed in [D3.js](https://d3js.org/).
* Python [Flask](http://flask.pocoo.org/) webserver on the back end.
* [Redis](http://redis.io/) store for passing JSON data between front and back.

##Further HTTP/2 Info

* [Official spec](https://github.com/http2/http2-spec)
* A helpful overview of [HTTP/2's origins and
development](https://www.smashingmagazine.com/2016/02/getting-ready-for-http2/)

