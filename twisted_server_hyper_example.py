"""
head_request.py
~~~~~~~~~~~~~~~
A short example that demonstrates a client that makes HEAD requests to certain
websites.
This example is intended as a reproduction of nghttp2 issue 396, for the
purposes of compatibility testing.
"""
from __future__ import print_function

from twisted.internet import reactor
from twisted.internet.endpoints import connectProtocol, SSL4ClientEndpoint
from twisted.internet.protocol import Protocol
from twisted.internet.ssl import optionsForClientTLS
from hyperframe.frame import SettingsFrame
from h2.connection import H2Connection
from h2.events import (
    ResponseReceived, DataReceived, RemoteSettingsChanged, StreamEnded,
    StreamReset, SettingsAcknowledged,
)


AUTHORITY = u'http2bin.org'
PATH = '/'
SIZE = 4096


class H2Protocol(Protocol):
    def __init__(self):
        self.conn = H2Connection()
        self.known_proto = b'h2'
        self.request_made = False
        self.frames = []

    def connectionMade(self):
        self.conn.initiate_connection()
        # This reproduces the error in #396, by changing the header table size.
        # self.conn.update_settings({SettingsFrame.HEADER_TABLE_SIZE: SIZE})

        self.transport.write(self.conn.data_to_send())
        print("connectionMade")

    def dataReceived(self, data):
        # if not self.known_proto:
            # self.known_proto = True
            # assert self.known_proto == b'h2'

        events = self.conn.receive_data(data)

        for event in events:
            self.frames.append(event)
            if isinstance(event, ResponseReceived):
                self.handleResponse(event.headers, event.stream_id)
            elif isinstance(event, DataReceived):
                self.handleData(event.data, event.stream_id)
            elif isinstance(event, StreamEnded):
                self.endStream(event.stream_id)
            elif isinstance(event, SettingsAcknowledged):
                self.settingsAcked(event)
            elif isinstance(event, StreamReset):
                reactor.stop()
                raise RuntimeError("Stream reset: %d" % event.error_code)
            else:
                print(event)

        #here is the problem--line 67--issuing bad requests.
        print(data)

        data = self.conn.data_to_send()
        if data:
            self.transport.write(data)



    def settingsAcked(self, event):
        # Having received the remote settings change, lets send our request.
        if not self.request_made:

            self.sendRequest()

    def handleResponse(self, response_headers, stream_id):

        for name, value in response_headers:
            print("%s: %s" % (name, value))

        print("")

    def handleData(self, data, stream_id):
        print(data, end='')

    def endStream(self, stream_id):
        self.conn.close_connection()
        self.transport.write(self.conn.data_to_send())
        self.transport.loseConnection()
        print(self.frames)
        reactor.stop()

    def sendRequest(self):
        request_headers = [
            (':method', 'GET'),
            (':authority', AUTHORITY),
            (':scheme', 'https'),
            (':path', PATH),
            ('user-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36)')
            ]
        self.conn.send_headers(1, request_headers, end_stream=True)
        self.request_made = True


options = optionsForClientTLS(
    hostname=AUTHORITY,
    # extraCertificateOptions={'nextProtocols': [b'h2']},
)

connectProtocol(
    SSL4ClientEndpoint(reactor, AUTHORITY, 443, options),
    H2Protocol()
)
reactor.run()