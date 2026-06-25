import json
from datetime import datetime

TRACE_FILE = "traces/traces.json"


def add_trace(step_name, status):

    trace = {
        "step": step_name,
        "status": status,
        "timestamp": str(datetime.now())
    }

    try:
        with open(TRACE_FILE, "r") as f:
            traces = json.load(f)

    except:
        traces = []

    traces.append(trace)

    with open(TRACE_FILE, "w") as f:
        json.dump(traces, f, indent=4)


def get_traces():

    try:
        with open(TRACE_FILE, "r") as f:
            return json.load(f)

    except:
        return []


def clear_traces():

    with open(TRACE_FILE, "w") as f:
        json.dump([], f, indent=4)