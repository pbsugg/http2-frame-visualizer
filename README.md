A small app for visualizing differences in performance and execution between HTTP/1.x new HTTP/2 standard.  Visualizations will be built in D3.js and other forms when necessary.  First tell will be a visualization of reduced header sizes in HTTP/2.  Workflow will be something like the following:

Backend written in Flask

Make header request using urllib2 or something similar
Fake a user-agent browser to simulate what it would look like in chrome, firefox, etc.
Read size (in bits) of all returned headers and create visual.
Show suitable comparison pages with average difference
