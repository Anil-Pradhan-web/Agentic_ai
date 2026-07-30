# Agentic AI Engineer Programme — Day 9 Session Notes
### CogniForce AI | Topic Focus: Beyond VS Code Copilot — Multi-Agent, Distributed & Remote Agentic Platforms
*Notes compiled on July 30, 2026*

> **Note on terminology:** The source audio/transcript repeatedly renders the tool name inconsistently (heard as "open claw," "open clock," "open cloud"). Based on the installation URL referenced in the session (`opencode.ai/installation`), this is almost certainly **OpenCode**, an open-source, model-agnostic agentic CLI/framework. It is referred to as **OpenCode** throughout these notes, with the instructor's spoken variant noted where relevant. A second platform, **"Multika,"** is mentioned only briefly as a future topic — its exact name/spelling could not be confirmed from the transcript.

---

## Chapter 1: Course Context & Mindset — AI-Augmented Problem Solving

- **Coding as a standalone skill is being displaced.** The instructor stresses that traditional software development tasks — writing code, unit tests, BRDs (Business Requirement Documents), and other execution work — are increasingly handled by AI tools (e.g., ChatGPT, GitHub Copilot in Visual Studio).
- **The learner's real job:** apply problem-solving technique *together with* AI to solve problems faster than manual development — not to write code from scratch.
- **Golden rule before starting any assignment:**
  - Do **not** start an assignment until you fully understand the problem statement/objective.
  - Starting without understanding wastes time, energy, cost ("token burn," "unnecessary dollar spend"), and typically results in a zero outcome.
  - Once the problem is genuinely understood, solving it (with AI assistance) should only take **10–30 minutes**.
- **Instructor's guidance for assignments:**
  1. Take the problem statement.
  2. Develop the use case.
  3. Develop the test case.
  4. Develop the code (using AI tools like ChatGPT / GitHub Copilot).
  5. Submit the completed work.
- **Participation reminder:** Students were encouraged to speak up (in English or Hindi) rather than just listen, as active participation/articulation builds clarity of thought — passive listening isn't sufficient for skill-building.

---

## Chapter 2: Skills & Skill Scanning in GitHub Copilot

- A **"skill"** in this context is an installable capability/package that can be injected into an AI coding agent (e.g., GitHub Copilot in Visual Studio) to improve its output quality for a specific type of task (e.g., a "design skill" for producing design documents/diagrams).
- **Skill Scanner:** A separate tool used to scan a downloaded skill for **vulnerabilities** before installing/deploying it.
  - If the scanner raises a vulnerability alert on a skill → the skill is **not safe to install**. Discard it and try a different skill.
  - If the scan shows **no vulnerabilities** → the skill is safe, and the underlying program/concept is validated as "working."
- **Recommended exercise/workflow:**
  1. Download a candidate skill.
  2. Run it through the skill scanner.
  3. If vulnerability-free → inject/install the skill into the agent (e.g., GitHub Copilot).
  4. Only after installation, issue prompts — the injected skill improves the quality of outputs (e.g., design diagrams, business process documents, use case diagrams).
- **Key insight:** The same prompt, on the same model, produces a noticeably weaker/inconsistent ("hanky panky") result **without** the skill, versus a much stronger result **with** the skill installed. This illustrates why skills matter.
- Clarification: "Open Claw/OpenCode," "skill," and "skill scanner" are **three separate, independent concepts/tools** — they are not the same thing and should not be conflated.

---

## Chapter 3: Limitations of VS Code / GitHub Copilot as an Agentic Platform

Visual Studio + GitHub Copilot supports building agents (Agent mode, Ask/Plan modes, model selection, tool selection), but has structural limitations that motivate moving to a platform like OpenCode:

| Limitation | Explanation |
|---|---|
| **Manual approval required per action** | The user must repeatedly grant permission for each step the agent wants to take. |
| **Machine/hardware dependency** | If the laptop is shut/put to sleep, the agent instance stops entirely — the CPU/memory enter a sleep state and nothing executes, regardless of platform. |
| **Single-machine/single-owner confinement** | An agent built in Visual Studio is tied to the laptop it was created on. To let a colleague reuse it, the code/config must be physically copied ("shipped") to their machine. |
| **No remote/mobile channel** | There is no way to interact with the agent via messaging apps (Telegram, WhatsApp, etc.) while away from the machine. |
| **Task-based, not goal-based** | The user acts as the orchestrator, manually invoking individual specialized agents (e.g., Java coding agent, .NET coding agent, BRD agent, testing agent) one at a time for specific tasks. There is no native way to hand off a broad **goal** to a master agent that automatically coordinates multiple sub-agents. |

- **Assigned task (Task 1)** — see Action Items section.

---

## Chapter 4: Introduction to OpenCode — Concept & Permission Model

- OpenCode is described as an **agentic framework/tool** (not just an app) for building and running AI agents outside the confines of a single IDE.
- **Correcting a misconception raised in class:** OpenCode is **not** a "no-permission-needed" system that runs entirely unsupervised. It still has an approval mechanism:
  - Default mode: **"approval preview"** — every action the agent wants to take must be explicitly approved by the human before execution.
  - The human can choose to **turn approval off** for a given agent once they trust it (e.g., after it has "delivered multiple times without misfiring"), effectively giving it blanket approval to proceed autonomously.
  - **No platform provides blanket approval by default** — this is a deliberate choice made by the user based on trust built over time.
- **Why permission-checking matters:** A human, before executing a destructive command (e.g., `delete`, dropping database records, deleting files), naturally pauses and thinks twice. **An agent does not have this innate caution** — it will find an instruction and apply it immediately. Therefore, agents must be designed to ask for confirmation before consequential actions (install, delete, rename, move files, etc.).
- **Core principle:** *"Agent is a doer. Human is the decision maker."* In any agentic platform, agents should not autonomously make high-stakes decisions unless a strong trust threshold has been reached.
- **Example scenario:** An agent trying to run a Node.js application realizes Node isn't installed and asks the human for permission to install it before proceeding.

---

## Chapter 5: Goal-Oriented Multi-Agent Orchestration

- **Key distinction: Task vs. Goal**
  - **Task** = a specific, narrow instruction given to one agent at a time (e.g., "run this test," "write this function"). This is what Visual Studio Copilot supports well.
  - **Goal** = a broad outcome the user wants delivered, requiring coordination across multiple specialized sub-agents. Visual Studio Copilot does **not** natively support this.

### Analogy 1 — Organizing a wedding
Two approaches to managing "my younger brother's wedding" (the goal):
1. **Self-orchestration:** You personally contact and coordinate the decorator, band, and catering agencies individually. You are the orchestrator.
2. **Full outsourcing:** You hand the entire goal to a single event-management agency. That agency internally manages/sub-contracts decoration, band, catering, etc. You only interact with one point of contact, and they deliver the complete outcome.

### Analogy 2 — Publishing a book
- A **main (master) agent** is given the overall goal of "publish this book."
- The main agent creates/coordinates **three sub-agents**: Author, Reviewer, and Compliance/Quality Checker.
- Sub-agents complete their specialized work and report back to the main agent, which consolidates and delivers the final result to the human.

### Core takeaway
- In a true multi-agent platform, the human allocates a **goal** to a **master/orchestrator agent**.
- The master agent creates and manages **sub-agents**, each specialized for a sub-task.
- Sub-agents return results to the master agent, which synthesizes a single, refined response back to the human.
- This orchestrator–sub-agent (master/child agent) relationship is what Visual Studio Copilot cannot natively deliver, but OpenCode (and similar platforms like **Hermes**) are designed for.

---

## Chapter 6: Distributed Agents Across Machines & Infrastructure

- Agents do **not** need to run on a single machine. Different agent **runtimes** (e.g., Claude, Codex, Hermes, OpenCode, GitHub Copilot, Trae) can each run on different individual machines belonging to different team members.
- **Illustrative setup discussed in class** (example agent/runtime-to-person mapping used by the instructor):

| Agent / Runtime | Example Machine/Owner |
|---|---|
| Claude | Ritu's laptop |
| Codex | Mohit's laptop |
| Hermes agent | Mandy's laptop |
| OpenCode | Akanksha's machine |
| Nova (agent) | Mohit's machine |
| Helix (agent) | Akanksha's machine |

- An **orchestrator/task-giver** can assign work to *any* of these agents regardless of which machine they run on — the system doesn't require centralizing everything on one box.
- **Real-world/industry example:** A "Vortex" agent running on US infrastructure, a "PM report" agent running on Australian infrastructure, and an "Estimation" agent running on Indian infrastructure can all be invoked by the same orchestrator. This is called **distributed computing / distributed agent execution**.
- **Requirement:** Only network **connectivity** is needed between the orchestrator and each agent runtime — physical co-location is not required.
- **Dashboard concept:** A central runtime configuration page lets an admin register an agent's infrastructure/IP address, see its status (on/off — e.g., "off" because the host laptop is asleep or the agent process isn't running), and manage ownership/access.

---

## Chapter 7: Data Sovereignty & the "Multika" Platform (Preview Only)

- **Data sovereignty:** Most countries require that their citizens' data be processed only within their own geographic/legal boundary (e.g., India's data should not leave India; the US and China have similar restrictions).
- Because agentic platforms often process sensitive data, a distributed multi-agent system must be able to **restrict where a given agent's processing happens** — e.g., "Nova" agent restricted to execute only on US infrastructure using US data; "Helix" restricted to China, using Chinese infrastructure only.
- This capability — enforcing geography-bound, compliant data processing per agent — is **not achievable within OpenCode alone**.
- A separate platform, referred to as **"Multika"** in the session, is planned to be covered in a future class specifically to address this data-sovereignty/compliance requirement. *(No further technical detail on Multika was given in this session — flagged here as a placeholder for later coverage.)*

---

## Chapter 8: Remote & Mobile Access via Channels (e.g., Telegram)

- A key differentiator of OpenCode over Visual Studio Copilot: it introduces the concept of a **"channel"** — a way to interact with a running agent without being physically present at the machine.
- **Example scenario walked through in class:**
  - You are the sole owner of a critical program and are on holiday, away from your laptop.
  - Your CEO/client calls about a production issue that must be fixed immediately.
  - You cannot delegate to teammates (you built the program) and cannot carry your laptop.
  - Because your laptop is left powered on at home (with automated sleep/shutdown disabled) and the OpenCode gateway is running, you can open a channel app on your **phone** (e.g., **Telegram**, WhatsApp) and message your agent directly.
  - The agent receives the message as a prompt/task, investigates the issue (e.g., is it a bug or a training/usage issue), and reports back — allowing you to make a decision and have the agent fix, recode, or confirm "working as designed," all remotely.
- This is described as **"truly agentic"** — you do not need to sit in front of the machine at all; you can be fully mobile.
- **Live demo detail:** The instructor typed a message from the Telegram mobile app ("Tell me which model you are using for this session") without touching the keyboard, and the same conversation/response appeared simultaneously in the desktop OpenCode session — demonstrating that the mobile channel and desktop instance share the same running agent session.
- Practical note: The instructor mentioned disabling the OpenCode **GUI/control dashboard** on their own machine because it was consuming virtual machine resources, preferring Telegram as the primary interaction channel instead.

---

## Chapter 9: Model Connectivity & Authentication

### 9.1 Model-agnostic connectivity
- OpenCode can connect to **any compatible model provider** — it is not locked into a single vendor (e.g., not limited to only OpenAI or only Anthropic/Claude models).
- Supported connection types include:
  - Commercial API providers (OpenAI, Anthropic, etc.)
  - **OpenRouter** — a single API key/subscription that provides access to many different LLM providers (open- and closed-source) without needing separate logins/subscriptions for each.
  - **Locally-run open-source models** via tools such as **Ollama, LM Studio, and Jan**. Configuration only requires:
    - The local server URL (e.g., `http://127.0.0.1:<port>`)
    - The model name being served
    - **No API key is required** for local models.
  - **Hugging Face API** — useful if you don't have high-end local hardware; lets you consume open-source models hosted on Hugging Face via subscription/API.

### 9.2 Authentication methods — OAuth vs. API Token
Two authentication approaches were compared in depth:

| Aspect | OAuth (Session-Based) | API Token (Token-Based) |
|---|---|---|
| **Mechanism** | Application "shakes hands" with another application; user logs in via email/password redirect to the provider's own login page (e.g., logging into OpenAI's page directly). | Application passes a token/secret string with every request; server validates the token before processing. |
| **Session lifecycle** | Session persists until the user logs out, the session times out, or is manually killed — no repeated validation needed during an active session. | Every single request/response must carry and re-validate the token; no persistent "session" concept. |
| **Implementation complexity** | More complex to implement (adds an extra security/handshake layer). | Simpler to implement. |
| **Security risk** | Sharing user ID/password compromises the account. | Sharing the token allows anyone to consume services/resources under your identity — tokens are highly sensitive and should never be shared. |
| **Cost/usage behavior (per instructor)** | With an OpenAI subscription + OAuth, usage tends to be more generous, allowing more tasks to be completed. | API token consumption is described as fast and expensive relative to OAuth-based subscription use. |
| **Anthropic/Claude-specific restriction** | **Anthropic/Claude does not permit OAuth authentication for third-party tools.** Only official API-token-based authentication is allowed. | If a request is detected as coming via unauthorized OAuth, Anthropic may **suspend or permanently disable** the account. This is presented as a real risk to be aware of. |

- **Practical guidance for setup:** Users with an OpenAI *subscription* can authenticate via OAuth directly through OpenCode's onboarding. Users without one can instead supply an **OpenRouter API key** or an **NVIDIA API key** and select an open-source model at no/low cost.

---

## Chapter 10: OpenCode Installation, Setup & Configuration Files

### 10.1 Installation environment
- Recommended to install inside **WSL (Windows Subsystem for Linux)** to avoid disturbing the native Windows environment, or directly on Linux/macOS.
- Requires a specific **Node.js** version as a prerequisite.
- Installation source referenced: **opencode.ai** → installation page → choose the CLI installer appropriate for your OS (Mac / Windows / Linux via WSL). A single CLI command performs the full installation.
- Alternative/advanced setup mentioned by a student: using a **headless Ubuntu server** instead of WSL is also viable for more advanced users.
- If installation via `curl` fails (e.g., "command not found"), the instructor's recommended fallback is to **ask an AI assistant (Claude, etc.) directly**, explicitly pointing it to the official installation URL (`opencode.ai/installation`) and specifying your OS, so it can walk you through prerequisite checks and step-by-step installation. The instructor's stance: *"There is no situation where AI cannot help you install this."*
- **Hardware guidance:** Running your own local model deployment comfortably benefits from **32GB RAM with an i7/i9 laptop**; otherwise, use API-based models (OpenRouter, NVIDIA, Hugging Face) instead of local deployment.

### 10.2 Core CLI commands
| Command (as referenced in session) | Purpose |
|---|---|
| `opencode onboard` | Launches the interactive setup wizard (first-time configuration: channel setup e.g. Telegram, and LLM authentication). |
| `opencode gateway start` | Starts the OpenCode gateway/runtime on the machine. |
| `opencode gateway start --port <port>` | Starts the gateway on a specific port. |
| `opencode gateway shut` | Shuts down the gateway (no agent access possible while down). |
| `opencode gateway restart` | Restarts the gateway after configuration changes. |
| `opencode logs` (with follow) | Streams/displays live logs — shows agent allocation/deallocation and request activity; useful for diagnosing errors. |
| `opencode doctor` | Built-in diagnostics tool — identifies configuration/installation issues. |
| `opencode doctor fix` | Automatically attempts to fix issues identified by the doctor command. |
| `opencode control` | Opens a GUI/dashboard version of the control panel (optional; can be resource-intensive on some machines — the instructor disabled it in favor of Telegram). |

### 10.3 Onboarding wizard flow
1. Optional channel configuration (e.g., Telegram) — can be skipped and configured later.
2. LLM authentication — choose OAuth (OpenAI subscription) **or** API key (OpenRouter, NVIDIA, Hugging Face, etc.).
3. Model selection (choose an open-source model if avoiding cost).

### 10.4 Workspace and configuration file architecture
- **Default agent:** On install, a default agent workspace is created automatically.
- **Per-agent workspaces:** Every additional agent created (examples used in session: *Helix, Iris, Nova, Nova Light, Nova Prime, Rex, Sage, Sar*) gets its **own isolated workspace**, ensuring no conflicts between agents' activities.
- **Per-agent Markdown (.md) configuration files** created by default for each agent (exact purpose of each to be covered in the next session):
  - `AGENTS.md` (or similar "collagent" bootstrap file — name unclear in transcript)
  - `heartbeat.md`
  - `identity.md`
  - `users.md`
  - `tools.md`
  - `soul.md`
  - (and related sub-configuration files)
  - *Instructor noted these files define fundamental agent behavior — e.g., what a "soul" agent means, what a "heartbeat" agent does, what the tools file governs — to be discussed in depth in the following class.*
- **`opencloud.json` (or equivalent config JSON):** Central configuration file for OpenCode itself — records the primary model, secondary model, and all settings configured via the CLI/onboarding wizard.
- **File transfer tip:** To move files between a WSL/Linux environment and Windows, the instructor recommended **WinSCP**.

---

## Action Items / Assignments

1. **Task 1 — VS Code Copilot Pros & Cons (individual/group slide):**
   - Prepare a single slide or one-pager listing the **top 5 positives** and **top 5 limitations** of developing and publishing agents in **Visual Studio / GitHub Copilot**.
   - Submit to the designated GitHub repository.
   - Group leaders are responsible for ensuring their entire team submits.

2. **Task 2 — OAuth vs. API Token comparison (individual/group write-up):**
   - Write **5 comparison points** between **session-based (OAuth) authentication** and **token-based (API) authentication**.
   - Include the pros and cons of each, and state **which is better and why** (technical justification required — not just financial/cost reasoning).
   - Submit to the designated GitHub repository.

3. **Install OpenCode ("Open Claw"):**
   - Install via WSL (or headless Ubuntu/Linux/macOS) following the official guide at `opencode.ai/installation`.
   - Complete the onboarding wizard: configure a channel (optional) and authenticate to an LLM provider (OAuth via OpenAI subscription, or API key via OpenRouter/NVIDIA/Hugging Face).
   - Confirm the installation is functioning (e.g., via `opencode doctor`, logs, or a test prompt).
   - This should be completed today or by the next session — students who are stuck are encouraged to ask an AI assistant for direct, step-by-step installation help.

4. **General reminder:** Do not attempt an assignment before fully understanding the problem statement/objective — clarify first, then execute.

---

## Execution Steps (OpenCode Setup Workflow)

1. Set up **WSL** (or a Linux/headless Ubuntu environment) if on Windows.
2. Visit **opencode.ai** and go to the installation/product ecosystem page.
3. Choose the correct installer for your OS (Mac / Windows-WSL / Linux) and run the single CLI install command.
4. Run `opencode gateway start` to initialize the gateway; the first run triggers the configuration prompts.
5. During onboarding:
   - Optionally configure a channel (e.g., Telegram) — can be skipped for now.
   - Choose your LLM authentication method:
     - **OAuth** (if you have an OpenAI subscription) — redirects to the provider login.
     - **API key** (OpenRouter, NVIDIA, or Hugging Face) — paste the key directly.
   - Select a model (prefer open-source/free models if avoiding cost).
6. Once running, use `opencode logs` to monitor activity, and `opencode doctor` / `opencode doctor fix` to diagnose and resolve issues.
7. Optionally open `opencode control` for a GUI dashboard, or configure a messaging channel (e.g., Telegram) for remote/mobile interaction.
8. Locate and review the auto-generated per-agent Markdown configuration files and the central config JSON (e.g., `opencloud.json`) for the default agent workspace — deeper exploration to follow in the next class.

---

## Key Takeaways

- **AI is now the primary "coder"** — the human's value lies in problem understanding, orchestration, and applying technique alongside AI, not manual code-writing.
- **Understand before you build.** Clarify the problem statement fully before starting; a well-understood problem is a fast (10–30 minute) solve.
- **Skills need vetting.** Always vulnerability-scan a skill before installing it into an agent; skills materially improve prompt outcomes when trustworthy.
- **VS Code Copilot is task-oriented and machine-bound**, which limits it for goal-oriented, distributed, or remote agentic work.
- **OpenCode enables goal-oriented multi-agent orchestration** — a master/orchestrator agent delegates to specialized sub-agents and consolidates their output.
- **Agents can run distributed across machines/geographies**, coordinated by a single orchestrator, requiring only network connectivity.
- **Data sovereignty is a real constraint** for distributed agent systems; a dedicated platform ("Multika") will address geography-bound compliant processing in a future session.
- **Remote/mobile control via channels (e.g., Telegram)** is a defining feature of true agentic platforms — you don't need to be at your machine to operate your agents.
- **OpenCode is model-agnostic**, supporting commercial APIs, OpenRouter, local models (Ollama/LM Studio/Jan), and Hugging Face-hosted models.
- **OAuth vs. API token is a critical technical distinction** — OAuth is session-based and provider-restricted (e.g., Anthropic disallows OAuth for third-party tools and risks account suspension for violations), while API tokens are simpler but consumed per-request and can be costly.
- **Agent permission/approval is not "free-for-all."** Every platform requires either per-action approval or an explicit, trust-based decision to disable it — the human remains the decision-maker.