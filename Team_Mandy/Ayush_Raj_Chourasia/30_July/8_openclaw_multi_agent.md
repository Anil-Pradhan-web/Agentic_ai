# OpenClaw Multi-Agent Team Creation

This guide details the creation of a 4-agent persistent marketing team (Nova, Sage, Iris, and Rex) inside OpenClaw, enabling them to communicate via `sessions_send`.

## 1. Workspace Initialization
We established 4 distinct agent IDs in `openclaw.json` (all using `gpt-4o` or equivalent):
- **Nova:** Orchestrator / Marketing Admin (Bound to Telegram bot)
- **Sage:** Content Creator (Social media focus)
- **Iris:** SEO & Research (Long-form blogs/newsletters)
- **Rex:** Analytics & Reporting (Data focused)

## 2. Directory Structure Setup
We created isolated workspaces for each agent to ensure clean context management:
```text
~/.openclaw/
 ├── workspace-nova/ (skills/, AGENTS.md, SOUL.md, memory.md)
 ├── workspace-sage/ (skills/, AGENTS.md, SOUL.md, memory.md)
 ├── workspace-iris/ (skills/, AGENTS.md, SOUL.md, memory.md)
 ├── workspace-rex/  (skills/, AGENTS.md, SOUL.md, memory.md)
 └── shared/         (meeting-memory.md, brand-context.md)
```

## 3. Tool Permissions
To allow the agents to talk to each other, we enabled the `sessions_send` tool in the global configuration:
```json
"tools": {
  "allow": ["sessions_list", "sessions_history", "sessions_send", "session_status"]
}
```

## 4. Role Definition (SOUL.md)
- **Nova:** Manages the team. Receives requests from the CEO via Telegram, reads `brand-context.md`, identifies the correct agent, and delegates.
- **Sage:** Responsible for short-form, punchy copy (X, Instagram, LinkedIn).
- **Iris:** Handles SEO research and 1000-word blog posts.
- **Rex:** Generates weekly data performance reports.

## 5. Skills Deployment
We deployed specific `.md` files into the `skills/` folder of each agent.
- Nova received `delegation.md` containing exact `sessions_send` syntax (e.g., `agent:sage:main`).
- Sage received `linkedin.md`, `twitter-x.md`.
- Iris received `seo-research.md`, `blog-post.md`.
- Rex received `analytics-report.md`.

## 6. Execution & Testing
When testing, we sent a message to Nova via Telegram: "Research the rise of fractional CTOs."
Nova successfully parsed the intent, used `sessions_send` to task Iris with SEO research, and reported back with the file path of the completed draft.
