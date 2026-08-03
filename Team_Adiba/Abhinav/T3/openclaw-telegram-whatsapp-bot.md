# OpenClaw Telegram and WhatsApp Bot
**Date:** 2026-08-02

---

# Objective
Explain how to connect Telegram and WhatsApp channels to an OpenClaw agent, and clarify WhatsApp auto-reply risks with a solution that limits replies to the user’s own number.

---

# Summary

- **Telegram and WhatsApp can both be frontends** for the same OpenClaw bot logic.
- **Telegram setup is straightforward** with BotFather, a token, and an OpenClaw Telegram connector.
- **WhatsApp setup requires a Cloud API or business gateway** and a configured phone number.
- **WhatsApp auto-reply can send responses to all incoming messages** if not restricted.
- **Use WhatsApp’s Message Yourself feature** or sender filtering to ensure the bot only replies to your own number.

---

# How the integration works

OpenClaw acts as the conversation orchestrator, while Telegram and WhatsApp provide external message channels. The bot receives incoming messages, processes them through OpenClaw skills, and sends outgoing text back through the same channel.

| Component | Telegram | WhatsApp |
|---|---|---|
| Channel type | Bot API | Cloud API / Business API / gateway |
| Auth | Bot token | Access token + phone ID |
| User identity | chat ID | sender phone number |
| Common pattern | webhook or polling | webhook event handling |

---

# Telegram setup

1. Create a bot with BotFather.
2. Save the bot token.
3. Configure OpenClaw to use the Telegram channel module, supplying the token and webhook or polling endpoint.
4. Define a skill that handles incoming messages and returns replies.

Example Telegram flow:

- User sends message to @YourBot
- Telegram forwards the update to OpenClaw
- OpenClaw executes the skill and returns text
- Telegram delivers the reply to the user

---

# WhatsApp setup and auto-reply warning

WhatsApp automation is more sensitive because WhatsApp may automatically reply to every incoming message on the registered number. If using a shared or public WhatsApp number, the bot can unintentionally respond to unknown contacts.

## Key risk

- **Auto-reply scope**: a WhatsApp bot attached to a number can reply to all messages sent to that number unless filtered.

## Safe solution using Message Yourself / sender filtering

- Use WhatsApp’s “Message Yourself” feature to create a dedicated chat with your own number.
- Configure the bot integration to only process messages when the sender matches your own phone number.
- If the channel receives messages from other numbers, ignore them.

Example filter logic:

```python
if incoming_message.sender != MY_PHONE_NUMBER:
    return None  # ignore messages from other users
```

This ensures the bot behaves like a personal assistant rather than an open auto-responder.

---

# Recommended OpenClaw architecture

- One OpenClaw skill handles the bot logic.
- A Telegram connector forwards Telegram updates into OpenClaw.
- A WhatsApp connector forwards WhatsApp webhook events into the same OpenClaw skill.
- Add sender validation for WhatsApp to prevent unwanted auto replies.

---

# Comparison Table

| Criterion | Telegram | WhatsApp |
|---|---|---|
| Ease of setup | Easier | More complex |
| Auto-reply risk | Low | High if not filtered |
| User identity control | Chat ID only | Phone number filtering required |
| Best use | public bot, group support | personal-only or business notifications |

---

# Recommendation

Use Telegram for general OpenClaw bot deployment and WhatsApp only when you need personal or business notifications with strict sender filtering. For WhatsApp, configure the integration to reply only to your own number and use Message Yourself as the primary chat to avoid auto-replying to unintended contacts.

---

# Next Steps

- Register and configure the Telegram bot token in OpenClaw.
- Set up WhatsApp Cloud API or gateway access and secure the webhook.
- Add sender filtering so WhatsApp replies only to the configured personal number.
- Test both channels with sample messages before enabling more users.
