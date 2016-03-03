# Objective

An app to visualize the mechanics of HTTP/2 streams in real-time.  Visualization stream built in D3.js, Python Flask backend.

## Goals of the project

 For a user (developer audience), I want the basic functionality of the http/2 protocol to become apparent at a glance.  When I make a GET request to a site, the user should immediately see the exchange of frames from client to user and vice-versa (see mockup_images).  BOTTOM LINE: What "value" do I add over another visualization service like chrome's "net-internals?"

### Project Components

#### Frames broken down by type--how to simulate frames?
     * A "stream" is horizontal flow--left to right, similar to this example in D3 gallery:
        http://bl.ocks.org/mbostock/raw/4060954/
     * Size (vertical width) of the stream shows how much data is coming through (when waiting for server push)
     * Data "packets" are bumps in the stream, sized according to the time they come in
     * I want an "open" stream to visually vibrate or "pulse" a bit, signaling it's still open
     * Information about each frame will appear below the stream itself.  
        Access more by clicking actual data, representative values, etc.

#### Reach
  * Request stream (just show response for now)
  * Other HTTP verbs besides GET
  * Stream multiplexing (multiple incoming streams--as they open)
