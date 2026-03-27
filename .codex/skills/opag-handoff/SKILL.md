---
name: opag-handoff
description: Continue development in the Open Personal AI Grid repository. Use when Codex needs to onboard onto the OPAG codebase, inspect the current minimal FastAPI agent and ledger demo, plan or implement the next iteration, or preserve the existing demo flow while extending tools, storage, workers, or architecture docs.
---

# OPAG Handoff

Use this skill to take over work in the OPAG repository with minimal rediscovery. Keep focus on the current runnable demo first, then align changes with the documented target architecture.

## Quick Start

1. Open the repo root and read `README.md` for the product framing.
2. Read `references/project-map.md` for the current code layout, runtime path, and known constraints.
3. Inspect the current execution chain before changing behavior:
   - `agent/server.py`
   - `tools/registry.py`
   - `tools/ledger.py`
4. Check git status before edits. The repo may be clean, but do not assume there are no user changes.

## Working Rules

- Preserve the existing demo route `POST /task` unless the user explicitly asks to redesign it.
- Treat the current codebase as a minimal prototype, not as a finished architecture.
- Prefer small, demonstrable improvements over speculative framework work.
- Keep implementation consistent with the roadmap and architecture docs, but do not build future layers unless the user asks for them.
- If adding behavior beyond the ledger demo, keep the registry pattern simple and explicit.

## Development Workflow

### Fix or extend the current demo

Use this path when the user asks for bug fixes, request parsing improvements, tool additions, or better persistence.

1. Start from `agent/server.py`.
2. Trace tool dispatch through `tools/registry.py`.
3. Check storage behavior in `tools/ledger.py` and `ledger.db`.
4. Verify whether `requirements.txt` and examples still match runtime behavior.
5. Prefer changes that can be verified with a small local command or request.

### Expand toward the intended architecture

Use this path when the user asks for workers, scheduler, plugins, memory, or broader system design.

1. Read `ARCHITECTURE.md` and `ROADMAP.md`.
2. Confirm whether the target is a prototype stub or a real implementation slice.
3. Add one layer at a time with clear boundaries.
4. Avoid creating empty abstractions unless they unlock an immediate next feature.

## Current Priorities

- The only implemented end-to-end flow is a simple expense-recording demo for requests containing the noodle keyword.
- `worker/worker.py` and `storage/db.py` are placeholders at the time this skill was created.
- The repo includes architecture and roadmap docs that are broader than the current implementation.
- `ledger.db` lives at the repo root and is used by `tools/ledger.py`.

## Verification

For small backend changes, prefer lightweight verification such as:

- importing helper functions with `python -c`
- checking fixed database paths
- reviewing `git diff`

If running the API server, ensure the route and example payload still match the README demo.

## Reference Files

- Read `references/project-map.md` before making larger changes.
