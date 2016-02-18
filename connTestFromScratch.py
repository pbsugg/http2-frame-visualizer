
# An attempt to build the connection from scratch

import h2.connection
AUTHORITY = u'http2bin.org'
PATH = '/'
stream_id = 1
data = 'hello'
from socket import socket
connection_socket = socket()

conn = h2.connection.H2Connection()
request_headers = [
    (':method', 'HEAD'),
    (':authority', AUTHORITY),
    (':scheme', 'https'),
    (':path', PATH),
    ('user-agent', 'hyper-h2/1.0.0'),
]
conn.send_headers(stream_id, headers=request_headers)
conn.send_data(stream_id, data)
connection_socket.sendall(conn.data_to_send())
events = conn.receive_data(socket_data)
