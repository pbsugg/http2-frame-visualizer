A small app for visualizing differences in performance and execution between HTTP/1.x new HTTP/2 standard.  Visualizations will be built in D3.js and other forms when necessary.  First tell will be a visualization of reduced header sizes in HTTP/2.  Workflow will be something like the following:

Backend written in Flask

2/10

Possible tasks to visualize

Header page sizes (with and w/o compression)
Build the request using HTTP/1.1 and HTTP/2 clients--keep conditions
Build different types of sites
Fake a user-agent browser to simulate what it would look like in chrome, firefox, etc.
Read size (in bits) of all returned headers
Create pyramid visual--2 sites inside one another, one with http/1, another w/ http/2

2/18 TD:

Get twisted server to receive any http2 website
Fork the repo and see if you can't tweak some of these methods to show a little more info (is this even possible?)
