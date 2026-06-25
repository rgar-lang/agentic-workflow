# Agentic Workflow Enterprise

## Overview

Agentic Workflow Enterprise is a proof-of-concept (POC) that demonstrates an enterprise-grade multi-agent workflow using FastAPI and Temporal.

The system orchestrates multiple AI agents through a durable workflow, provides structured execution traces, exposes REST APIs for monitoring, supports real-time status streaming, and is designed to be extended with isolated execution environments such as Firecracker microVMs or gVisor for production deployments.

---

# Architecture

```
                +----------------------+
                |      FastAPI         |
                |   REST API Layer     |
                +----------+-----------+
                           |
                           |
                    POST /run
                           |
                           |
                +----------v-----------+
                |  Workflow Orchestrator|
                +----------+-----------+
                           |
                 Planner Activity
                           |
          -------------------------------
          |                             |
          |                             |
    Worker Activity 1             Worker Activity 2
          |                             |
          -------------------------------
                           |
                    Reviewer Activity
                           |
                +----------v-----------+
                | Trace Manager        |
                | Status Manager       |
                +----------+-----------+
                           |
              --------------------------
              |                        |
         /status API             /traces API
              |
          Streaming API
```

---

# Technology Stack

- Python 3.11
- FastAPI
- Temporal Workflow
- Temporal Worker
- Temporal Client
- Docker
- Pydantic
- Pytest
- AsyncIO

---

# Features

- Multi-Agent Workflow
- Planner Agent
- Parallel Worker Agents
- Reviewer Agent
- Temporal Durable Workflow
- Activity Retry Policy
- Activity Timeout Strategy
- FastAPI REST APIs
- Structured Langfuse-style Execution Traces
- Workflow Status Monitoring
- Server-Sent Event (SSE) Streaming
- Docker Support
- Unit Test Framework

---

# Project Structure

```
AgenticWorkflow/

├── activities/
│   ├── planner_activity.py
│   ├── worker_activity.py
│   └── reviewer_activity.py
│
├── api/
│   ├── main.py
│   └── routes.py
│
├── models/
│   ├── request_model.py
│   ├── response_model.py
│   ├── status_model.py
│   └── trace_model.py
│
├── streaming/
│   ├── status_manager.py
│   └── status_stream.py
│
├── traces/
│   └── trace_manager.py
│
├── temporal/
│   ├── worker.py
│   ├── client.py
│   └── agent_workflow.py
│
├── workflows/
│   └── multi_agent_workflow.py
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Workflow Execution

```
Planner

↓

Worker 1
      \
       \
        ---> Reviewer

Worker 2
```

Execution Order:

1. Planner Agent starts.
2. Planner completes.
3. Worker 1 and Worker 2 execute in parallel.
4. Reviewer validates outputs.
5. Workflow completes.
6. Execution traces are recorded.
7. Workflow status is updated.

---

# Temporal Workflow

The workflow is implemented using Temporal and provides:

- Durable execution
- Retry Policy
- Activity Timeouts
- Parallel Activity Execution
- Workflow History
- Workflow Monitoring
- Fault Tolerance

---

# Retry Strategy

Each activity is configured with:

- Maximum Attempts: 3
- Start-to-Close Timeout
- Schedule-to-Close Timeout

This enables automatic retries for transient failures.

---

# REST APIs

## Health Check

```
GET /health
```

Returns application health.

---

## Run Workflow

```
POST /run
```

Executes the complete multi-agent workflow.

---

## Workflow Status

```
GET /status
```

Returns the current workflow execution status.

Example

```json
{
    "current_step": "completed",
    "status": "completed"
}
```

---

## Execution Traces

```
GET /traces
```

Returns Langfuse-style execution traces.

Example

```json
[
    {
        "step": "planner",
        "status": "running",
        "timestamp": "2026-06-25 11:20:15"
    },
    {
        "step": "planner",
        "status": "completed",
        "timestamp": "2026-06-25 11:20:20"
    }
]
```

---

## Status Streaming

```
GET /stream
```

Provides real-time workflow status updates using Server-Sent Events (SSE).

---

# Running the Application

## Install Dependencies

```
pip install -r requirements.txt
```

---

## Start Temporal Server

```
docker compose -f temporal/docker-compose-temporal.yml up
```

---

## Start Temporal Worker

```
python -m temporal.worker
```

---

## Execute Workflow

```
python -m temporal.client
```

---

## Start FastAPI

```
python -m uvicorn api.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

## Temporal UI

```
http://localhost:8233
```

---

# Docker

Build and run the application

```
docker compose up --build
```

---

# Testing

Run all tests

```
pytest
```

Current test modules

- test_workflow.py
- test_agents.py
- test_trace.py
- test_api.py

---

# Production Considerations

For local development, agent execution runs directly within the Python process.

For production environments, untrusted execution can be isolated using:

- Firecracker MicroVMs
- gVisor Containers
- Docker Sandbox

The workflow orchestration remains unchanged while only the execution backend changes.

---

# Future Enhancements

- Firecracker integration
- Langfuse integration
- OpenTelemetry tracing
- PostgreSQL persistence
- Redis cache
- Authentication & Authorization
- Kubernetes deployment
- Prometheus metrics
- Grafana dashboards
- AI Agent Plugin Framework

---

# Demo Flow

1. Open Temporal UI.
2. Execute workflow using Swagger.
3. Observe Planner → Workers → Reviewer execution.
4. View workflow history in Temporal.
5. View execution traces.
6. Monitor workflow status.
7. Demonstrate parallel worker execution.
8. Explain retry strategy and durable workflow.

---

# Author

**Rathnakar Gardas**

Senior Full Stack QA Engineer

Enterprise Agentic Workflow POC