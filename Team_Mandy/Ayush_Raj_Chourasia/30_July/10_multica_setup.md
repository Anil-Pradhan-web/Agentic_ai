# 🌐 Multica Setup and Configuration

Multica is an advanced multi-agent orchestration and deployment platform. Setting it up locally allows us to manage massive agent swarms visually rather than relying strictly on terminal scripts.

## 1. Prerequisites
- Docker & Docker Compose
- Minimum 16GB RAM for local multi-agent simulations
- Python 3.10+

## 2. Downloading Multica
The easiest way to set up Multica is via their official Docker image.

```bash
git clone https://github.com/multica-ai/multica-core.git
cd multica-core
```

## 3. Environment Configuration
Copy the default environment file and populate your keys:
```bash
cp .env.example .env
```
Ensure you include:
- `OPENAI_API_KEY` (or local endpoint URL)
- `MULTICA_ENV=development`
- `DATABASE_URL=postgres://user:pass@localhost:5432/multica`

## 4. Launching the Services
Run the full stack (Frontend, Backend, Postgres, and Redis) using Docker Compose:

```bash
docker-compose up -d --build
```
Wait for the containers to initialize. Check logs if needed:
```bash
docker-compose logs -f
```

## 5. Dashboard Onboarding
1. Navigate to `http://localhost:3000` in your browser.
2. Create your admin account.
3. Under **Swarm Configurations**, you can visually drag and drop agents, link them with communication channels (like `sessions_send`), and assign them shared memory drives.
4. **Integration with OpenClaw:** Multica can act as a higher-level orchestrator that sends REST triggers to OpenClaw workspaces on a scheduled cron job.
