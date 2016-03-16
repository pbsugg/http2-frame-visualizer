

from h2.events import (
    ResponseReceived, DataReceived, RemoteSettingsChanged, StreamEnded,
    StreamReset, SettingsAcknowledged,RequestReceived   
)
import json

testObject = RequestReceived()
testObject.stream_id = 1
testObject.headers = {"test": "hello"}


# sort the object by type
# give it to the method with the right encoding method

class FrameEventToJSON(JSONEncoder):

    def default(self, event):

        if isinstance(event, RequestReceived):
            return {"stream_id": event.stream_id,
                    "headers": event.headers}
        # elif isinstance(event, DataReceived):
        # elif isinstance(event, RemoteSettingsChanged):
        # elif isinstance(event, StreamEnded):
        # elif isinstance(event, StreamReset):
        # elif isinstance(event, SettingsAcknowledged):
        # elif isinstance(event, RequestReceived):
    


print(json.dumps(testObject, cls=FrameEventToJSON))
