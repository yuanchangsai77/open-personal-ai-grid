# Open Personal AI Grid (OPAG)

Open-source infrastructure for running a **personal AI agent network** using local devices and open models.开源个人 AI 算力与智能代理平台

## Vision

AI systems today rely heavily on centralized cloud services.

OPAG aims to build a **self-hosted personal AI infrastructure** that:

- runs local AI models
- utilizes idle devices as compute nodes
- provides a unified AI agent interface
- keeps all data private and auditable

## Core Features

- Local AI model inference
- Distributed compute nodes
- Tool calling system
- Event logging and audit
- Self-hosted deployment

## Architecture

User Device
↓
Agent Server
↓
Scheduler
↓
Worker Nodes
↓
Tools

## Example

User input:

记一笔吃米线14元

Agent:

ledger.add_expense(
 item="米线",
 amount=14
)

## Roadmap

See ROADMAP.md

## License

MIT
