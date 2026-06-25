import time
import json
from streaming.status_manager import workflow_status

def event_generator():

    while True:
        yield f"data: {json.dumps(workflow_status)}\n\n"
        time.sleep(1)