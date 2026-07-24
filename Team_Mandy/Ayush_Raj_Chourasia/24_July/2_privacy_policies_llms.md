# Privacy Policies of Major LLM Providers: A Comparative Analysis

As organizations and individuals increasingly rely on Large Language Models (LLMs), understanding how top providers handle user data is critical. This document compares the privacy policies of **OpenAI (ChatGPT/GPT-4)**, **Google (Gemini)**, and **Anthropic (Claude)**.

---

## 1. OpenAI (ChatGPT & API)

OpenAI distinguishes between its consumer products (like ChatGPT Free/Plus) and its enterprise/API offerings.

### Consumer (ChatGPT Free/Plus)
- **Data Training:** By default, OpenAI **may use** your conversations to train and improve its models.
- **Opt-Out:** Users can opt out by turning off "Chat History & Training" in the settings, or by submitting a privacy request form.
- **Data Retention:** Chats are retained for 30 days for abuse monitoring, even if training is disabled.

### Enterprise / API
- **Data Training:** OpenAI **does not** use data submitted via its API, ChatGPT Enterprise, or ChatGPT Team for training its models.
- **Data Retention:** API inputs/outputs are retained for 30 days for trust and safety purposes, but enterprise clients can request zero data retention (ZDR) for eligible endpoints.

---

## 2. Google (Gemini & Vertex AI)

Google also separates its consumer-facing Gemini apps from its enterprise Google Cloud (Vertex AI) services.

### Consumer (Gemini Web App)
- **Data Training:** Google **uses** conversations, location data, and feedback to improve its products, including training its foundational models.
- **Human Review:** A subset of conversations is read, annotated, and processed by human reviewers to improve quality. These are disconnected from the user's Google Account but retained for up to 3 years.
- **Opt-Out:** Users can turn off "Gemini Apps Activity." If turned off, conversations are kept for 72 hours for safety purposes but not used for training.

### Enterprise (Google Cloud Vertex AI)
- **Data Training:** Google explicitly states that it **does not** use customer data (prompts or responses) submitted to Vertex AI to train its foundation models.
- **Privacy:** Enterprise data remains strictly within the customer's cloud boundary, adhering to enterprise compliance standards (e.g., HIPAA, SOC).

---

## 3. Anthropic (Claude & API)

Anthropic positions itself as a safety-first and privacy-conscious AI company.

### Consumer (Claude.ai Web App)
- **Data Training:** Unlike OpenAI and Google, Anthropic states that it **does not** use user prompts or outputs to train its models by default. They only use data for training if a user explicitly clicks the "thumbs down" button to provide feedback and consents to it.
- **Data Retention:** Chats are retained in the user's account history until deleted by the user.

### Enterprise / API
- **Data Training:** Anthropic **never** uses API data to train its models.
- **Data Retention:** API data is retained for 30 days for abuse prevention. Like OpenAI, Anthropic offers zero data retention (ZDR) policies for enterprise customers who require it.

---

## Conclusion & Summary

| Feature | OpenAI (ChatGPT) | Google (Gemini App) | Anthropic (Claude.ai) | Enterprise/API (All 3) |
| :--- | :--- | :--- | :--- | :--- |
| **Trains on User Data?** | Yes (Opt-out available) | Yes (Opt-out available) | No (Opt-in via feedback) | **No** |
| **Human Review?** | Rare / Safety only | Yes (for sampled data) | Rare / Safety only | No (Unless legally required) |
| **Best For Privacy** | Moderate | Lowest (Strict tracking) | Highest (No default training) | Highest (Enterprise SLAs) |

**Key Takeaway:** For sensitive data, businesses should **never** use consumer web apps (ChatGPT, Gemini). They should strictly use the **API** or **Enterprise tiers**, which universally prohibit model training on customer data.
