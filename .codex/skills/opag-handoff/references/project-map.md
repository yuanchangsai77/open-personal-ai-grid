# Project Map

## Repo Root

Expected repo root during development:

- `E:\company\yuan\opag\open-personal-ai-grid`

## Product Intent

OPAG means Open Personal AI Grid. The documented goal is a self-hosted personal AI infrastructure that can run local models, use idle devices as compute nodes, expose a unified agent interface, and keep data private and auditable.

The current implementation is much smaller than the vision. Treat docs as target state and code as an early prototype.

## Current Runnable Path

The main implemented path is:

1. Client sends `POST /task` to the FastAPI app in `agent/server.py`.
2. `run_task()` looks for a hard-coded food keyword.
3. `extract_amount()` pulls the first integer from the user text.
4. `tools.registry.call_tool()` dispatches to `ledger.add_expense`.
5. `tools/ledger.py` writes the expense into the SQLite database at repo-root `ledger.db`.

## Important Files

### Runtime code

- `agent/server.py`: FastAPI entrypoint and current intent parsing.
- `tools/registry.py`: minimal tool registry and dispatcher.
- `tools/ledger.py`: SQLite-backed ledger write path.
- `examples/demo_request.py`: minimal request example.
- `requirements.txt`: Python dependencies for the prototype.

### Docs

- `README.md`: project overview and demo example.
- `ARCHITECTURE.md`: target high-level system layout.
- `ROADMAP.md`: intended staged evolution from minimal agent to broader AI infrastructure.
- `docs/project.md`: longer Chinese project description.

### Placeholders or not yet implemented

- `worker/worker.py`: empty placeholder.
- `storage/db.py`: empty placeholder.

## Current Constraints

- Tool routing is hard-coded in a Python dict, not schema-driven.
- Request understanding is string-matching plus regex extraction, not model-based planning.
- Only one demo tool is implemented.
- There are no automated tests in the repo at the time this skill was created.
- Changes should avoid breaking the existing `POST /task` demo unless the user asks for a redesign.

## Recent Practical Fixes Already Landed

These behaviors are already present in the repo state this skill reflects:

- amount is parsed from user text instead of being hard-coded to `14`
- SQLite uses a fixed repo-root database path instead of cwd-relative path
- database writes use a context manager
- `requests` is listed in `requirements.txt` for the example client

## Recommended Next-Step Strategy

Choose one of these tracks based on the user's request:

### Track 1: Stabilize the prototype

Use when the user asks for bug fixing, cleanup, better parsing, tests, or small feature work.

Good candidates:

- add tests for amount parsing and tool dispatch
- improve request parsing for more expense phrases
- return structured API errors
- add read/query endpoints for stored expenses

### Track 2: Add a second real tool

Use when the user wants the registry to become meaningful without over-engineering.

Good candidates:

- category support for ledger entries
- simple note tool
- local file read/write tool with constraints

### Track 3: Build toward architecture docs

Use when the user explicitly asks for scheduler, worker nodes, plugins, or distributed execution.

Recommended approach:

- implement thin vertical slices
- avoid broad abstractions with no runtime path
- document what remains stubbed versus functional

## Validation Tips

- On Windows shell, use explicit UTF-8 when reading Chinese text in repo files to avoid false encoding alarms.
- Prefer `python -c` checks for helpers and path resolution.
- When reviewing or committing, use `git -c safe.directory=E:/company/yuan/opag/open-personal-ai-grid ...` if git safe-directory warnings appear in sandboxed environments.
