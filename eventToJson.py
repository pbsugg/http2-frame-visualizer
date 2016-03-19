

from h2.events import (
    ResponseReceived, DataReceived, RemoteSettingsChanged, StreamEnded,
    StreamReset, SettingsAcknowledged,RequestReceived   
)
from h2.events import _bytes_representation
import json

# sort the object by type
# give it to the method with the right encoding method

class FrameEventToJSON(json.JSONEncoder):

    def default(self, event):

        if isinstance(event, RequestReceived):
            return {"stream_id": event.stream_id,
                    "headers": event.headers}
        elif isinstance(event, DataReceived):
            return {"stream_id": event.stream_id,
            "flow_controlled_length": event.flow_controlled_length,
            "data": event.data}
        elif isinstance(event, RemoteSettingsChanged):
            return {"changed_settings": event.changed_settings}
        # elif isinstance(event, StreamEnded):
        # elif isinstance(event, StreamReset):
        elif isinstance(event, SettingsAcknowledged):
            return {"changed_settings": event.changed_settings}
        elif isinstance(event, ResponseReceived):
            return {"stream_id": event.stream_id,
            "headers": self.parse_response_headers_to_JSON(event)} 

    # return the header object as a series of pairs in dictionary 
    def parse_response_headers_to_JSON(self, event):
        headers = event.headers
        return_dict = {}
        for header_pair in headers:
            return_dict[header_pair[0]] = header_pair[1]
        return return_dict

            
    
