# 🤖 Agent Integration with Telegram Bot

Instead of testing an agent purely via the CLI, binding it to a Telegram bot allows for real-time testing, mobile access, and a more user-friendly interface. Here is the process to set up a Telegram bot for OpenClaw/Custom agents.

## 1. Create the Bot via BotFather
1. Open Telegram and search for `@BotFather`.
2. Send the command `/newbot`.
3. Provide a name (e.g., `Ayush AI Agent`) and a username (e.g., `ayush_agent_bot`).
4. BotFather will provide an **HTTP API Token** (e.g., `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`). **Keep this secure!**

## 2. Obtain Your Account ID
To ensure the bot only responds to you, you need your Telegram Account ID.
1. Search for `@userinfobot` in Telegram.
2. Send `/start`.
3. Note your `Id` (e.g., `987654321`).

## 3. Bind the Bot in OpenClaw
Open your `openclaw.json` (or equivalent `.env` config) and update the binding section:

```json
"bindings": {
  "telegram": {
    "token": "YOUR_TELEGRAM_API_TOKEN",
    "accountId": "YOUR_TELEGRAM_ACCOUNT_ID"
  }
}
```

## 4. Testing the Bot
1. Start your OpenClaw gateway:
   ```bash
   python gateway.py --host 0.0.0.0 --port 8000
   ```
2. Open your Telegram bot and send a test message: `"Hello Nova, what is your status?"`
3. The agent should receive the message via the gateway and reply directly into the Telegram chat!

> **Security Note:** Always restrict the `accountId` array so the bot ignores messages from unauthorized Telegram users.
