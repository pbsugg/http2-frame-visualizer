

"""
fixed ssl with "acceptableProtocols in twisted, see this:"
http://twisted.readthedocs.org/en/latest/core/howto/ssl.html
"""

import os 
#twisted imports
from twisted.internet import reactor
from twisted.internet.endpoints import connectProtocol, SSL4ClientEndpoint
from twisted.internet.ssl import optionsForClientTLS
# my twisted files
from twisted_client import H2Protocol

# for passing messages
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 
from messageHandler import messageHandler


SIZE = 4096
AUTHORITY = u'twitter.com'
PATH = '/'

def run(messagehandler): 

    options = optionsForClientTLS(
        hostname=AUTHORITY,
        acceptableProtocols=[b'h2', b'http/1.1'],
    )

    connectProtocol(
        SSL4ClientEndpoint(reactor, AUTHORITY, 443, options),
        H2Protocol(messagehandler)
    )

    reactor.run(installSignalHandlers=0)


