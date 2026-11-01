# SeifNuker Protocol Suite 🛡️

> **High-Throughput Discord Gateway Security & Rate-Limit Benchmark Harness**

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![asyncio](https://img.shields.io/badge/Framework-asyncio_%26_aiohttp-2C5BB4?style=for-the-badge)](https://docs.python.org/3/library/asyncio.html)
[![Gateway](https://img.shields.io/badge/Discord_Gateway-v10-5865F2?style=for-the-badge&logo=discord)](https://discord.com/developers/docs/topics/gateway)
[![License: Educational](https://img.shields.io/badge/License-Educational_Research-red.svg?style=for-the-badge)](LICENSE)

An educational cybersecurity research tool engineered to stress-test Discord bot gateways, rate-limit recovery curves, and server permission models under simulated high-concurrency conditions. Built to identify rate-limit bucket vulnerabilities (HTTP 429 backoff kinetics), privilege escalation cascades, and anti-raid defense velocities.

---

> [!CAUTION]
> **Educational & Research Purpose Only**: This tool is designed strictly for authorized stress-testing, defensive auditing, and academic exploration of distributed rate-limiting algorithms. Never execute against servers without explicit administrative authorization.

---

## ⚡ Core Capabilities

- **Low-Level WebSocket Dispatcher**: Connects directly to Discord Gateway v10 bypassing high-level library abstraction overhead.
- **Rate-Limit Bucket Telemetry**: Accurately measures sliding-window rate limits across Global, Per-Route, and Per-Guild HTTP 429 buckets.
- **Proxy Rotation Harness**: High-speed proxy pool rotation supporting massive concurrent requests with zero socket drops.
- **Disaster Recovery Simulation**: Benchmarks the speed and efficacy of defensive anti-raid bots under heavy automated load.

---

## 🚀 Setup & Execution

### 1. Requirements
- Python 3.11+
- Virtual environment recommended

### 2. Installation
```bash
git clone https://github.com/xSeiff/seifnuker-protocol-suite.git
cd seifnuker-protocol-suite
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate
pip install aiohttp colorama
```

### 3. Execution
```bash
python main.py
```

---

## 📜 License
Provided strictly for educational, security auditing, and resilience research purposes.

Authored by [Seif (@xSeiff)](https://github.com/xSeiff).
