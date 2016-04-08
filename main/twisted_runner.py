

"""
fixed ssl with "acceptableProtocols in twisted, see this:"
http://twisted.readthedocs.org/en/latest/core/howto/ssl.html
"""

from twisted.internet import reactor
from twisted.internet.endpoints import connectProtocol, SSL4ClientEndpoint
from twisted.internet.ssl import optionsForClientTLS

from messageHandler import messageHandler
from twisted_client import H2Protocol

SIZE = 4096
AUTHORITY = u'twitter.com'
PATH = '/'

options = optionsForClientTLS(
    hostname=AUTHORITY,
    acceptableProtocols=[b'h2', b'http/1.1'],
)

handler = messageHandler()

connectProtocol(
    SSL4ClientEndpoint(reactor, AUTHORITY, 443, options),
    H2Protocol(handler)
)

def run():
    reactor.run(installSignalHandlers=0)

