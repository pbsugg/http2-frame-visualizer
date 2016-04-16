"""
head_request.py
~~~~~~~~~~~~~~~
A short example that demonstrates a client that makes HEAD requests to certain
websites.
This example is intended as a reproduction of nghttp2 issue 396, for the
purposes of compatibility testing.

my notes:
TD: Add more frame options from h2.events
TD: Deal with sites that "hang"--provide a termination signal after pre-determined point
TD: Some sites still fail--redirects, etc.
"""
from __future__ import print_function
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

from hyperframe.frame import SettingsFrame
from h2.connection import H2Connection
from h2.events import (
    ResponseReceived, DataReceived, RemoteSettingsChanged, StreamEnded,
    StreamReset, SettingsAcknowledged,
)
import json

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 

from messageHandler import messageHandler

SIZE = 4096
AUTHORITY = u'twitter.com'
PATH = '/'

class H2Protocol(Protocol):
    def __init__(self, messageHandler):
        self.conn = H2Connection()
        self.known_proto = b'h2'
        self.request_made = False
        self.messageHandler = messageHandler

    def connectionMade(self):
        self.conn.initiate_connection()
        # This reproduces the error in #396, by changing the header table size.
        self.conn.update_settings({SettingsFrame.HEADER_TABLE_SIZE: SIZE})
        self.transport.write(self.conn.data_to_send())

    def dataReceived(self, data):
        # TOFIX: Figure out how to get this method to work.
        # if not self.known_proto:
            # self.known_proto = True
            # assert self.known_proto == b'h2'

        events = self.conn.receive_data(data)

        for event in events:
            self.messageHandler.storeEvent(event)
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
        print(self.messageHandler.responseFrames)
        reactor.stop()

    def sendRequest(self):
        request_headers = [
            (':method', 'GET'),
            (':authority', AUTHORITY),
            (':scheme', 'https'),
            (':path', PATH),
            ('user-agent', 'Mozilla/5.0 (Macintosh; Intel Max OS X 10_11_3) App'),
            ('accept', 'application/json, text/javascript'),
            ]

        self.conn.send_headers(1, request_headers, end_stream=True)
        self.request_made = True

