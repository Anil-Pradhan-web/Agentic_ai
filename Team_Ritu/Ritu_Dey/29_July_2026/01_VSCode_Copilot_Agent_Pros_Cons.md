# Developing with an AI Agent in Visual Studio (Copilot) — Positives & Negatives

GitHub Copilot in Visual Studio / VS Code acts as an in-editor AI pair programmer. In its base form it suggests completions as you type; in **agent mode** it can plan and execute multi-file edits, run terminal commands, and iterate against errors on its own — closer to a junior developer working a ticket than an autocomplete engine.

## Positive

- **Speed on boilerplate** — repetitive code (CRUD handlers, DTOs, test scaffolding, config files) gets generated in seconds instead of typed by hand.
- **Context-aware suggestions** — agent mode reads across the open workspace, not just the current file, so suggestions match existing naming conventions and patterns instead of generic ones.
- **Multi-step task execution** — it can chain edits, run the build/test command, read the failure output, and patch again without a human manually copy-pasting errors back in.
- **Lower barrier for unfamiliar code/APIs** — it can explain a function or draft a first attempt at an unfamiliar framework, shortening the research loop before writing real code.
- **Built-in tool access** — running tests, git commands, and linters as part of its own loop catches some mistakes before a human ever reviews the diff.

## Negative

- **Confident but wrong code** — it can produce plausible-looking logic that is subtly incorrect (off-by-one errors, missed edge cases), which is more dangerous than obviously broken code because it's easy to trust without close review.
- **Security blind spots** — it can suggest insecure patterns (string-concatenated SQL, missing input validation, hard-coded secrets) unless explicitly guided or reviewed.
- **Scope creep in agent mode** — a loosely worded instruction can lead it to touch more files than intended, so every diff needs to be checked before accepting.
- **Skill atrophy risk** — over-reliance can weaken a developer's own debugging and design instincts, especially for beginners still building fundamentals.
- **Cost/latency** — agent-mode tasks that loop (edit → build → fix → rebuild) consume more time/tokens than a single autocomplete, and depend on network/service availability.
- **Data exposure** — project code is sent to the model provider; sensitive or proprietary codebases need a policy review before enabling agent features broadly.

## Takeaway

It's most valuable as an accelerant for well-scoped, reviewable work — not as an unsupervised replacement for code review or architectural judgment. Treat every agent-produced diff the way you'd treat a junior developer's PR: useful, fast, but not merge-worthy without a second look.
