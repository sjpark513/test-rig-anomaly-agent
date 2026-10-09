# Test Rig Anomaly Agent

An LLM agent that helps engineers investigate anomalies on durability and performance test rigs.
When a rig raises an alarm, the agent reads the sensor data, searches the test procedures and past failure cases,
and drafts a report with likely causes and a checklist of what to inspect first.

> **Status:** Phase 1 of 6 — structured extraction of alarm and test logs (Oct 2026). The project is built in public, one phase at a time.

## Why this project

Test rigs produce alarms and logs faster than anyone can read them. Finding the cause still means
switching between live sensor values, historical data, procedure documents and old failure reports.
This project explores how far an LLM agent can take that work, and how to prove with numbers when it is right or wrong.

## Roadmap

| Phase | Weeks | Capability | Component added |
| --- | --- | --- | --- |
| 1 | Oct 12 – Nov 1 | Model APIs, structured output | Extractor that turns alarm/test logs into JSON |
| 2 | Nov 2 – Dec 6 | RAG | Search over procedures and failure history, with citations |
| 3 | Dec 7 – Jan 10 | Tool use, agents | Sensor lookup, anomaly detection, report writer; Modbus link to a simulated rig |
| 4 | Jan 11 – Feb 7 | Evaluation, cost, security | Eval set with automatic scoring, regression tests, prompt-injection defense |
| 5 | Feb 8 – Mar 7 | Serving, operations | FastAPI service, Streamlit dashboard, deployment, tracing |
| 6 | Mar 8 – Apr 11 | Wrap-up | Final README, demo video, write-ups |

## Data policy

No internal documents, test data or drawings from any employer are used.
- **Sensor data:** public datasets (e.g. NASA C-MAPSS, CWRU bearing data) and a self-built rig simulator.
- **Documents:** test procedures, inspection manuals and failure cases written from general knowledge and experience.

## Project structure

```
src/test_rig_agent/   Python package (Phase 1: alarm/log schema and extractor)
data/samples/         Hand-written sample alarm and test logs
docs/retro/           Weekly retrospectives
tests/                Unit tests
```

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
cp .env.example .env    # add your API keys; .env is never committed
pytest
```

## Results

Measured results (extraction accuracy, retrieval hit rate, cost per request) will be added here as each phase is completed.

## License

MIT
