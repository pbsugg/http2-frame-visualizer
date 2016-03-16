import pytest
import sys
sys.path.append('../')
from h2.events import *
from eventToJson import FrameEventToJSON
import json
    
def test_RequestReceivedJSON():
    testObject = RequestReceived()
    testObject.stream_id = 1
    testObject.headers = [1,2,3]
    assert (json.dumps(testObject, cls=FrameEventToJSON) == 
            json.dumps({"stream_id":testObject.stream_id,"headers": 
             testObject.headers}))
