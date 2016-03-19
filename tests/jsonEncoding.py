import pytest
import sys
sys.path.append('../')
from h2.events import *
from h2.events import _bytes_representation
from eventToJson import FrameEventToJSON
import json
from h2.settings import ChangedSetting
    
def test_RequestReceivedJSON():
    request_event = RequestReceived()
    request_event.stream_id = 1
    request_event.headers = [1,2,3]
    assert (json.dumps(request_event, cls=FrameEventToJSON) == 
            json.dumps({"stream_id":request_event.stream_id,"headers": 
             request_event.headers})
            )

def test_DataReceivedJSON():
    data_event = DataReceived()
    data_event.stream_id = 1
    data_event.flow_controlled_length = 400
    data_event.data = "ThisIsTestData"
    assert (json.dumps(data_event, cls=FrameEventToJSON) == 
            json.dumps({"stream_id": data_event.stream_id,
            "flow_controlled_length": data_event.flow_controlled_length,
            "data": data_event.data})
            )
    
def test_RemoteSettingsChangedJSON():
    remote_settings_event = RemoteSettingsChanged()
    remote_settings_event.changed_settings = ( ChangedSetting(setting=1, 
            original_value=4000,
            new_value = 5000)
            )
    assert (json.dumps(remote_settings_event, cls=FrameEventToJSON) == 
            json.dumps({"changed_settings":
            remote_settings_event.changed_settings})
            )

def test_SettingsAcknowledgedJSON():
    settings_event = SettingsAcknowledged()
    settings_event.changed_settings = ( ChangedSetting(setting=5, 
            original_value=1,
            new_value = "bob")
            )
    assert (json.dumps(settings_event, cls=FrameEventToJSON) == 
            json.dumps({"changed_settings": settings_event.changed_settings})
            )

def test_StreamEnded():
    end_event = StreamEnded()
    end_event.stream_id = 1
    assert(json.dumps(end_event, cls=FrameEventToJSON) ==
            json.dumps({"stream_id": end_event.stream_id}) 
            )

def test_ResponseReceivedJSON():
    response_event = ResponseReceived()
    response_event.stream_id = 1
    response_event.headers = [("status", 200),("cache-control", "no-cache"),
       ('content-encoding', 'gzip'), ('content-length', '29404') ]
    assert (json.dumps(response_event, cls=FrameEventToJSON) == 
            json.dumps({"stream_id": response_event.stream_id,
                "headers": {
                response_event.headers[0][0]:response_event.headers[0][1],
                response_event.headers[1][0]:response_event.headers[1][1],
                response_event.headers[2][0]:response_event.headers[2][1],
                response_event.headers[3][0]:response_event.headers[3][1]
                            }
                        }
                   )
            )
            

