# OpenClaw Installation and Setup Guide

OpenClaw is a framework for orchestrating autonomous AI agents. This guide covers the complete configuration and onboarding process.

## 1. Prerequisites
- Python 3.10+
- Node.js 18+ (for frontend dashboard)
- An active API key (OpenAI, Anthropic, or local LM Studio endpoint)

## 2. Installation Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/openclaw/openclaw.git
   cd openclaw
   ```

2. **Backend Setup (Python):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup (React):**
   ```bash
   cd frontend
   npm install
   npm run build
   ```

## 3. Configuration & Onboarding
1. **Environment Variables:**
   Copy the example config and edit it.
   ```bash
   cp .env.example .env
   ```
   Add your primary LLM API key: `OPENAI_API_KEY=sk-xxxx`

2. **Initialize the Database:**
   OpenClaw uses SQLite by default for managing agent memories.
   ```bash
   python manage.py migrate
   ```

3. **Launch the Gateway:**
   The gateway acts as the orchestrator for all agent communication.
   ```bash
   python gateway.py --host 0.0.0.0 --port 8000
   ```

4. **Onboarding:**
   Navigate to `http://localhost:8000` to access the OpenClaw dashboard. From here, you can define your first agent's "Soul" (personality), bind it to a messaging platform, and grant it basic skills (like web search).
