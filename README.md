# Agentic Workflow Enterprise

A production-style multi-agent orchestration platform built using **Temporal**, **FastAPI**, and **Python**.

This project demonstrates how multiple AI agents can collaborate through a durable, retryable workflow while exposing REST APIs for execution, monitoring, and tracing.

---

# Features

- Multi-Agent Workflow
- Temporal Workflow Orchestration
- FastAPI REST APIs
- Parallel Worker Execution
- Langfuse-style Execution Traces
- Streaming Status Endpoint
- Docker Sandbox Support
- Retry & Timeout Strategy
- Modular Architecture
- Unit Tests
- GitHub Ready

---

# Architecture

```
                 +----------------+
                 |    Planner     |
                 +----------------+
                          |
                          |
              ------------------------
              |                      |
              ▼                      ▼
       +-------------+        +-------------+
       |  Worker-1   |        |  Worker-2   |
       +-------------+        +-------------+
              |                      |
              ------------------------
                          |
                          ▼
                 +----------------+
                 |    Reviewer    |
                 +----------------+
                          |
                          ▼
                    Workflow Complete
```

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming Language |
| FastAPI | REST API |
| Temporal | Workflow Orchestration |
| Docker | Sandbox Isolation |
| AsyncIO | Parallel Agent Execution |
| Pytest | Testing |
| JSON | Trace Storage |

---

# Project Structure

```
AgenticWorkflow
│
├── activities/
│     planner_activity.py
│     worker_activity.py
│     reviewer_activity.py
│
├── agents/
│     planner_agent.py
│     worker_agent.py
│     reviewer_agent.py
│
├── api/
│     main.py
│     routes.py
│
├── config/
│
├── models/
│
├── sandbox/
│     Dockerfile
│     sandbox_manager.py
│
├── streaming/
│     status_manager.py
│     status_stream.py
│
├── temporal/
│     agent_workflow.py
│     worker.py
│     client.py
│
├── traces/
│     trace_manager.py
│
├── workflows/
│     multi_agent_workflow.py
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

The workflow follows this sequence:

```
Planner
   ↓
Worker-1  ||  Worker-2
   ↓
Reviewer
   ↓
Completed
```

Worker-1 and Worker-2 execute **in parallel** using **asyncio.gather()**.

---

# Installation

Clone the repository

```bash
git clone https://github.com/rgar-lang/agentic-workflow.git
```

Navigate into the project

```bash
cd agentic-workflow
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Start Temporal

```bash
docker compose -f temporal/docker-compose-temporal.yml up -d
```

Verify Temporal UI

```
http://localhost:8233
```

---

# Start Temporal Worker

```bash
python -m temporal.worker
```

Expected Output

```
Temporal Worker Started
```

---

# Start FastAPI

```bash
python -m uvicorn api.main:app --reload
```

Open Swagger

```
http://localhost:8000/docs
```

---

# Execute Workflow

Execute

```
POST /run
```

Expected Response

```json
{
    "planner": {
        "step": "planner",
        "status": "completed"
    },
    "worker1": {
        "step": "worker-1",
        "status": "completed"
    },
    "worker2": {
        "step": "worker-2",
        "status": "completed"
    },
    "reviewer": {
        "step": "reviewer",
        "status": "completed"
    },
    "workflow_status": "completed"
}
```

---

# API Endpoints

## Health Check

```
GET /health
```

Returns

```json
{
    "status":"healthy"
}
```

---

## Execute Workflow

```
POST /run
```

Starts the complete Planner → Worker → Reviewer workflow.

---

## Workflow Status

```
GET /status
```

Returns

```json
{
    "current_step":"completed",
    "status":"completed"
}
```

---

## Workflow Traces

```
GET /traces
```

Returns Langfuse-style execution traces.

Example

```json
[
  {
    "step":"planner",
    "status":"running"
  },
  {
    "step":"planner",
    "status":"completed"
  },
  {
    "step":"worker-1",
    "status":"running"
  },
  {
    "step":"worker-2",
    "status":"running"
  },
  {
    "step":"worker-1",
    "status":"completed"
  },
  {
    "step":"worker-2",
    "status":"completed"
  },
  {
    "step":"reviewer",
    "status":"running"
  },
  {
    "step":"reviewer",
    "status":"completed"
  }
]
```

---

## Streaming Endpoint

```
GET /stream
```

Streams workflow execution updates.

---

# Temporal Features

This implementation uses Temporal for durable workflow execution.

Implemented capabilities include:

- Durable Workflow Execution
- Retry Policy
- Timeout Handling
- Parallel Activities
- Worker Orchestration
- Workflow History
- Workflow Replay

Retry Configuration

```python
RetryPolicy(
    maximum_attempts=3
)
```

Timeouts

```
Start-To-Close Timeout

Schedule-To-Close Timeout
```

---

# Langfuse-style Tracing

Each activity records structured execution events.

Example

```
Planner Running

Planner Completed

Worker-1 Running

Worker-2 Running

Worker-1 Completed

Worker-2 Completed

Reviewer Running

Reviewer Completed
```

These traces can be retrieved using

```
GET /traces
```

---

# Docker Sandbox

The project contains a Docker sandbox module to isolate untrusted code execution.

Purpose

- Secure execution
- Isolation
- Multi-tenant readiness
- Independent runtime

Location

```
sandbox/
```

---

# Testing

Run all tests

```bash
pytest
```

Tests include

- Agent Tests
- API Tests
- Workflow Tests
- Trace Tests

---

# Future Improvements

- Redis Event Streaming
- Kafka Integration
- Langfuse Integration
- OpenTelemetry
- Kubernetes Deployment
- Authentication & Authorization
- Multi-Tenant Support
- LLM Integration
- Agent Memory
- Human Approval Workflow

---

# Repository

GitHub

https://github.com/rgar-lang/agentic-workflow

---

# Author

**Rathnakar Gardas**

Senior Full Stack QA Engineer

Automation | AI | Agentic Workflows | Temporal | FastAPI | Python

---