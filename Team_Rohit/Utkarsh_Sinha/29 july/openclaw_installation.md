# OpenClaw Installation, Setup & Onboarding Guide

## Executive Summary
OpenClaw is a modular, high-performance local agent runtime and multi-agent framework designed to orchestrate autonomous AI agents with full environment integration (file system tools, terminal execution, web search, and custom API integrations). This document provides a complete setup, configuration, and onboarding walkthrough.

---

## 1. System Requirements & Prerequisites

Prior to installing OpenClaw, ensure your environment meets the following dependencies:

| Dependency | Minimum Version | Recommended Version | Purpose |
| :--- | :--- | :--- | :--- |
| **Node.js** | v18.0.0+ | v20.x LTS | Core runtime engine |
| **Python** | 3.10+ | 3.11 / 3.12 | Tool execution environment |
| **Git** | 2.30+ | Latest | Version control & repository cloning |
| **Package Manager** | npm v9+ / pnpm v8+ | pnpm / yarn | Dependency installation |
| **API Provider** | OpenAI / Anthropic / Local | GPT-4o / Claude 3.5 / Ollama | Foundational LLM backend |

---

## 2. Step-by-Step Installation Guide

### Step 1: Clone Repository or Install CLI Package

#### Option A: Installing via Global CLI Package (Recommended)
```bash
# Install OpenClaw globally using npm
npm install -g openclaw@latest

# Verify installation
openclaw --version
```

#### Option B: Cloning Source Code (Development Setup)
```bash
# Clone the official repository
git clone https://github.com/openclaw/openclaw.git
cd openclaw

# Install dependencies
npm install

# Build project assets
npm run build

# Link binary locally
npm link
```

---

## 3. Environment & Configuration Setup

OpenClaw requires environment variables and a structured configuration file to operate safely and connect to model providers.

### Step 1: Create Environment Variables (`.env`)
Create a `.env` file in your workspace directory:

```env
# ===================================
# OpenClaw Core Configuration
# ===================================
OPENCLAW_ENV=development
OPENCLAW_PORT=8080
OPENCLAW_LOG_LEVEL=info
OPENCLAW_WORKSPACE=/Users/utkarshsinha/Documents/Agentic_ai/Team_Rohit/Utkarsh_Sinha/workspace

# ===================================
# Primary Model Provider Keys
# ===================================
OPENAI_API_KEY=sk-proj-your-actual-openai-api-key
ANTHROPIC_API_KEY=sk-ant-your-actual-anthropic-api-key

# ===================================
# Local Model Fallback (Optional)
# ===================================
OLLAMA_BASE_URL=http://localhost:11434
LOCAL_MODEL=llama3.2:3b

# ===================================
# Security & Sandbox Controls
# ===================================
ALLOW_TERMINAL_EXECUTION=true
ALLOW_FILE_SYSTEM_WRITE=true
REQUIRE_HUMAN_APPROVAL=false
```

### Step 2: Create Agent Configuration (`openclaw.config.json`)
Create `openclaw.config.json` in your configuration path:

```json
{
  "version": "1.0.0",
  "project": {
    "name": "UtkarshAgent Workspace",
    "owner": "Utkarsh Sinha"
  },
  "agent": {
    "name": "UtkarshClawAgent",
    "role": "Autonomous Software Engineer & Researcher",
    "model": "gpt-4o",
    "temperature": 0.1,
    "max_tokens": 4096,
    "system_prompt": "You are OpenClaw Agent, an expert AI engineer capable of analyzing codebases, executing terminal commands safely, and solving complex tasks."
  },
  "tools": [
    {
      "name": "file_system",
      "enabled": true,
      "config": {
        "read_allowed": true,
        "write_allowed": true,
        "base_path": "./"
      }
    },
    {
      "name": "terminal",
      "enabled": true,
      "config": {
        "timeout_ms": 30000,
        "blocked_commands": ["rm -rf /", "mkfs", "dd"]
      }
    },
    {
      "name": "web_browser",
      "enabled": true,
      "config": {
        "headless": true
      }
    }
  ]
}
```

---

## 4. Interactive Onboarding Wizard

OpenClaw includes an interactive onboarding wizard to automate credential validation and workspace setup:

```bash
# Launch interactive onboarding CLI
openclaw init
```

### Onboarding Steps Flow:
1. **Model Selection:** Choose primary LLM backend (OpenAI, Anthropic Claude, or Local Ollama).
2. **Credential Audit:** Validates API key authentication and network latency.
3. **Sandbox Configuration:** Sets security limits on terminal execution and file modification boundaries.
4. **Workspace Binding:** Binds the current directory `/Users/utkarshsinha/Documents/Agentic_ai/Team_Rohit/Utkarsh_Sinha` as the active operational sandbox.

---

## 5. Verification & Testing

To confirm OpenClaw is completely configured and ready for production tasks:

```bash
# 1. Run environment diagnostics check
openclaw doctor

# Expected Output:
# [✓] Node.js environment: v20.x verified
# [✓] API Credentials: OpenAI connected (HTTP 200 OK)
# [✓] Workspace Sandbox: Read/Write permissions granted
# [✓] Configuration file: openclaw.config.json valid

# 2. Execute a test task via CLI
openclaw run --prompt "Summarize workspace directory structure and generate a health report."
```

---

## 6. Summary Checklist
- [x] Node.js & Git installed
- [x] OpenClaw repository cloned / CLI package installed
- [x] `.env` file configured with valid API credentials
- [x] `openclaw.config.json` configured with tools & safety bounds
- [x] `openclaw doctor` diagnostics passed clean
