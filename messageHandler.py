#Goals
# Hold all request data as it's assembled
# Hold all response data as it's assembled 
# Put that data in a dict so can be passed further up the chain
from h2.events import (
    RequestReceived, ResponseReceived, DataReceived, RemoteSettingsChanged, StreamEnded,
    StreamReset, SettingsAcknowledged,
)

class messageHandler():

    def __init__(self):
        self.requestFrames = [] 
        self.responseFrames = [] 
    
    def storeEvent(self, event, response=True):
        if response == True:
            response = self.packageResponseEvent(event)
            self.responseFrames.append(response)

    def packageResponseEvent(self, event):

        if isinstance(event, RequestReceived):
            return  {"type": "RequestReceived", "stream_id": event.stream_id,
                    "headers": event.headers}
        elif isinstance(event, DataReceived):
            return {"type": "DataReceived", 
                    "stream_id": event.stream_id, 
                    "flow_controlled_length": event.flow_controlled_length,
                    "data": "Hello"}
        elif isinstance(event, RemoteSettingsChanged):
            return {"type": "RemoteSettingsChanged", 
                    "changed_settings": event.changed_settings}
        elif isinstance(event, StreamEnded):
            return {"type": "StreamEnded", "stream_id" : event.stream_id}
        # elif isinstance(event, StreamReset):
        elif isinstance(event, SettingsAcknowledged):
            return {"type": "SettingsAcknowledged", 
                    "changed_settings": event.changed_settings}
        elif isinstance(event, ResponseReceived):
            return {"type": "ResponseReceived", "stream_id" : event.stream_id,
                    "headers": self.parse_response_headers_to_JSON(event)} 


    # return the header object as a series of pairs in dictionary 
    def parse_response_headers_to_JSON(self, event):
        headers = event.headers
        return_dict = {}
        for header_pair in headers:
            return_dict[header_pair[0]] = header_pair[1]
        return return_dict
