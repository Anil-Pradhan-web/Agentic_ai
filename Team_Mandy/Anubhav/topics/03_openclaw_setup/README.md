# OpenClaw — Setup & Onboarding (Complete Configuration)

Files in this folder:

| File | Purpose |
|---|---|
| [`install.sh`](install.sh) | End-to-end setup script: system deps → clone → venv → install → configure → verify |
| [`.env.example`](.env.example) | Environment/config template (model provider, credentials, port, agent tool permissions) |
| [`agent.config.yaml`](agent.config.yaml) | Sample per-agent tool-permission config, same pattern as this repo's [`research.agent.md`](../../.github/agents/research.agent.md) |

## Prerequisites

- Git
- Python 3.10+ (venv module)
- An API key / OAuth credentials for the LLM provider backing the agent

## Run

```bash
chmod +x install.sh
./install.sh
```

The script:
1. Updates system packages and installs build deps (`build-essential`, `curl`, `git`, `pkg-config`, `libssl-dev`).
2. Clones the OpenClaw repo (or pulls latest if already present).
3. Creates and activates a Python virtual environment.
4. Installs Python dependencies from `requirements.txt`.
5. Copies `.env.example` → `.env` (only if `.env` doesn't already exist, so it never overwrites real config).
6. Runs a basic import check to confirm the install landed correctly.

## After running

1. Edit the generated `.env` with real values — model provider key/OAuth credentials, port, and which agent tools (`browser`/`terminal`/`edit`) are permitted. See [`02_OAuth_vs_APIKey_Pros_Cons.md`](../02_OAuth_vs_APIKey_Pros_Cons.md) for which auth style fits which use case.
2. Adjust `agent.config.yaml` per agent — keep `terminal` and `edit` disabled unless the agent genuinely needs to run commands or write files (least privilege).
3. Start the service:
   ```bash
   source .venv/bin/activate
   python3 -m openclaw start   # or the project's documented entrypoint
   ```
4. Verify it's running:
   ```bash
   ps aux | grep openclaw
   ```
5. Smoke-test with a simple prompt to confirm the model connection and tool permissions behave as configured.

## Common issues

| Issue | Likely cause | Fix |
|---|---|---|
| `Permission denied` / missing GPG keys during `apt-get update` | Stale package source lists | Re-run `sudo apt-get update` after refreshing sources; add missing GPG keys if prompted |
| Missing Python/Node modules after install | Interrupted or partial `pip install` | Re-run `pip install -r requirements.txt` inside the activated venv |
| Port already in use on start | Another process bound to the configured `PORT` | Change `PORT` in `.env`, or stop the conflicting process |

## Security notes

- `.env` is never committed — only `.env.example` (placeholders) belongs in git.
- Default `agent.config.yaml` disables `terminal` and `edit` tools; enable them only for agents that are actually trusted to run commands or write files.
- If installing third-party skills, scan them first (e.g. with NVIDIA SkillSpector) before granting them tool access.
