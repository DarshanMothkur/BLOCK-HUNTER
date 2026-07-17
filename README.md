# Block Hunter

### IIoT Cybersecurity Platform using Federated Learning, MLP & Blockchain

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)



**Block Hunter** is an M.Tech research project that builds a privacy-preserving **Industrial Internet of Things (IIoT)** cybersecurity platform. It combines:

| Component | Role |
|-----------|------|
| **MLP (Multi-Layer Perceptron)** | On-device / edge anomaly & intrusion detection |
| **Federated Learning (FL)** | Collaborative model training without sharing raw sensor data |
| **Blockchain** | Immutable logging of threats, model updates, and audit trails |
| **Flask** | REST API + web dashboard for operators |

---

## Architecture Overview

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  IIoT Devices   │────▶│  Edge FL Clients │────▶│  FL Aggregator  │
│  (sensors/PLC)  │     │  (local MLP)     │     │  (FedAvg)       │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
                        ┌─────────────────────────────────┼────────┐
                        │                                 ▼        │
                        │  ┌────────────┐         ┌──────────────┐ │
                        │  │  Flask API │◀───────▶│  Blockchain  │ │
                        │  │  + Web UI  │         │  Threat Log  │ │
                        │  └─────┬──────┘         └──────────────┘ │
                        │        │                                  │
                        │        ▼                                  │
                        │  ┌────────────┐                           │
                        │  │  SQLite DB │                           │
                        │  └────────────┘                           │
                        └──────────────────────────────────────────┘
```

---

## Features

- **Threat Detection** — MLP classifier for **Normal**, **DDoS Attack**, and **Packet Hijacking**
- **Federated Learning** — Multi-client FedAvg training; raw data stays on edge nodes
- **Blockchain Audit Trail** — SHA-256 chained blocks for detections, FL rounds, and alerts
- **Operator Dashboard** — Clean cards and tables for devices, monitoring, threats, FL status, blockchain explorer
- **Auth & RBAC-ready** — Login/register with secure password hashing
- **Reports & Alerts** — Historical reports and real-time alert feed

---

## Project Structure

```
Block-Hunter/
├── app.py                 # Flask application entry point
├── requirements.txt
├── LICENSE
├── README.md
├── frontend/              # HTML templates + static assets
│   ├── *.html
│   └── static/css|js
├── backend/               # Flask blueprints, services, utils
├── ml/                    # MLP model + federated learning
├── blockchain/            # Lightweight blockchain for audit logs
├── database/              # Models, init scripts, SQLite
├── datasets/              # Sample & processed IIoT datasets
├── models/                # Saved model weights / checkpoints
├── docs/                  # Architecture & API documentation
└── screenshots/           # UI captures for thesis / demo
```

---

## Quick Start

### 1. Prerequisites

- Python **3.10+**
- pip / venv

### 2. Install

```bash
cd E:\Block-Hunter
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
# source venv/bin/activate

pip install -r requirements.txt
```

### 3. Initialize database & sample data

```bash
python -c "from database.init_db import init_database; init_database()"
```

### 4. Run the server

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

| Demo account | Password   |
|--------------|------------|
| `admin`      | `admin123` |
| `operator`   | `ops123`   |

---

## Core Modules

### Machine Learning (`ml/`)

- `models/mlp_detector.py` — PyTorch/sklearn-compatible MLP for intrusion detection
- `federated/client.py` — Local training client (edge node)
- `federated/server.py` — FedAvg aggregator
- `preprocessing/pipeline.py` — Feature scaling & encoding for IIoT traffic

### Blockchain (`blockchain/`)

- Immutable chain of threat events and FL model hashes
- Simple proof-of-work (configurable difficulty) for demo integrity

### Backend API (`backend/`)

REST endpoints under `/api/v1/` for devices, threats, FL rounds, blockchain blocks, and alerts.

---

## API Snapshot

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/login` | Authenticate user |
| GET | `/api/v1/devices` | List IIoT devices |
| GET | `/api/v1/threats` | Detected threats |
| POST | `/api/v1/fl/start-round` | Start FL training round |
| GET | `/api/v1/blockchain/chain` | Full blockchain |
| GET | `/api/v1/alerts` | Active alerts |
| GET | `/api/v1/dashboard/stats` | Dashboard KPIs |

See [docs/API.md](docs/API.md) for full reference.

---



Suggested experimental metrics: accuracy, precision/recall/F1, communication cost, FL convergence rounds, and chain integrity verification.

---

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Setup Guide](docs/SETUP.md)

---



---

## Author

**Block Hunter** — R DARSHAN

*Federated Learning × Blockchain × Industrial IoT Security*


## Technologies Used
- Python + Flask
- PyTorch / Scikit-learn (MLP)
- Federated Learning
- Blockchain (custom implementation)
- SQLite

## What I Learned
- Privacy-preserving ML using Federated Learning
- Building lightweight blockchain for audit logs
- Full-stack development with Flask
