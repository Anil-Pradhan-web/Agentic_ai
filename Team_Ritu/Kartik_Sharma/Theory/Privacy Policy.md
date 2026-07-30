# Privacy Policies of Major LLM Providers — Focus: Claude (Anthropic)

*Last verified: July 30, 2026. Privacy policies change frequently — always check the official pages linked at the end before making decisions based on this document.*

---

## 1. Anthropic (Claude) — Detailed

### Consumer plans: Claude Free, Pro, Max

| Question | Answer |
|---|---|
| **Does Claude train on my chats by default?** | Yes, since a policy change effective **September 28, 2025**. Training is now **opt-out** rather than opt-in for consumer accounts. |
| **How do I opt out?** | Claude.ai → **Settings → Privacy → "You can help improve Claude"** toggle → turn off. |
| **What happens if I opt in (leave it on)?** | Anthropic may use your chats and coding sessions (including Claude Code sessions on consumer accounts) to improve its models. |
| **Retention if opted in** | Up to **5 years** — a large jump from the previous 30-day standard. This also applies to thumbs-up/down feedback you submit. |
| **Retention if opted out** | Conversations remain in your account until you delete them; once deleted, they persist on Anthropic's backend for up to **30 days** before permanent deletion, and are not used for training. |
| **Does the setting apply retroactively?** | No. It only applies to **new or resumed** chats and coding sessions from the point you set your preference. Old, untouched chats are not pulled into training. |
| **Safety review exception** | Conversations flagged for safety review may still be used/analyzed to improve abuse-detection and Safeguards-team models, regardless of your training toggle. |
| **Incognito chats** | Not used for training, even if your main privacy toggle is on. |

### Business / commercial products: Claude for Work, Team, Enterprise, API, Bedrock, Vertex AI

- These are **excluded** from the consumer training changes above and are governed by separate commercial terms.
- Standard **API log retention is 7 days** (reduced from 30 days in September 2025); API data is **not used for training** by default, with no exceptions on the standard tier. Organizations needing longer retention for auditing can opt into 30 days.

### July 2026 policy update (consumer)

Anthropic published a further Consumer Privacy Policy update effective **July 8, 2026**, which:
- Adds explicit language allowing Anthropic to request **age or identity verification** from users.
- Adds provisions for **data sharing during agentic AI tasks** (e.g., when Claude acts on your behalf in a browser or tool).
- Permits Anthropic to proactively share conversation data with **law enforcement** based on an internal "good faith belief" standard, without necessarily requiring a court order first — a notable change flagged by outside commentators.

### Independent assessment

One third-party privacy-scoring site (Privacy Watchdog, methodology-based, not legal advice) rated Anthropic's published policy **65/100 (Grade B-)** as of mid-2026 — the highest score among major AI providers reviewed, but still short of an "A."

---

## 2. OpenAI (ChatGPT) — Summary for Comparison

| Question | Answer |
|---|---|
| **Default for Free/Plus/Pro accounts** | Training is **on by default**; you must manually opt out. |
| **How to opt out** | Settings → Data Controls → "Improve the model for everyone" → toggle off. Applies to new conversations only, not retroactively. |
| **Standard retention even after opt-out** | Up to **30 days** for abuse monitoring; only Zero Data Retention (ZDR), an Enterprise-only feature, removes this. |
| **Temporary Chat** | Not used for training and deleted after 30 days, but still transmitted to and processed on OpenAI's servers during the session. |
| **Business tiers (Enterprise, Team, API)** | Not trained on by default; contractual Data Processing Addendums (DPAs) available. |
| **Litigation note** | A federal court order (NYT copyright litigation, S.D.N.Y.) required OpenAI to produce a de-identified sample of 20 million ChatGPT logs in January 2026, which OpenAI's own Data Controls FAQ now flags as a factor that could affect standard retention timelines. |
| **Independent score** | Same third-party site rated OpenAI's policy **48/100 (Grade C)**. |

---

## 3. Google (Gemini) — Summary for Comparison

| Question | Answer |
|---|---|
| **Default retention (consumer)** | **18 months**, adjustable to 3 or 36 months in account settings. |
| **Controlled via** | "Gemini Apps Activity" in your Google Account (myaccount.google.com → Data & Privacy), not a simple in-chat toggle. |
| **Human review** | A portion of conversations may be sampled for human review; any conversation touched by a reviewer is retained for up to **3 years** regardless of your general retention setting. |
| **Ecosystem integration** | Gemini can connect to Gmail, Calendar, Drive, and other Google services under a "Personal Intelligence" feature — opt-out by default in the US, opt-in by default in the EU under GDPR. |
| **Business tiers (Workspace, Vertex AI, Gemini Enterprise)** | Google states it will not train or fine-tune models on customer data without permission; short-term caching (e.g., 24 hours) may still occur for latency reasons. |

---

## 4. Side-by-Side Snapshot

| | Anthropic (Claude) | OpenAI (ChatGPT) | Google (Gemini) |
|---|---|---|---|
| Consumer training default | Opt-out (on) since Sep 2025 | Opt-out (on) | Opt-out (on) in US; opt-in in EU for cross-app features |
| Where to turn off | In-chat Settings → Privacy | Settings → Data Controls | Google Account → Data & Privacy |
| Max retention if opted in | 5 years | ~30 days (short-term), longer under litigation hold | 18 months default, up to 3 years if reviewed |
| Retention if opted out | ~30 days | ~30 days (still, for abuse monitoring) | Depends on "Keep Activity" setting |
| API/business default | Not trained on; 7-day log retention | Not trained on; up to 30-day retention | Not trained on; short caching only |
| Independent grade (Privacy Watchdog) | B- (65/100) | C (48/100) | Not scored in same review |

---

## 5. Practical Takeaways

1. **All three major consumer AI products now default to "on" for training** — this is an industry-wide shift, not unique to any one company. If you care about this, check settings on all platforms you use.
2. **Business/paid-individual accounts are not automatically private.** "Pro"-tier subscriptions (Claude Pro, ChatGPT Plus, Gemini Advanced) are generally treated like free accounts for privacy purposes — only Team/Enterprise/API tiers with signed agreements offer stronger default protections.
3. **Opting out is not retroactive.** Changing your setting only protects new conversations going forward.
4. **Opting out doesn't mean instant deletion.** All three providers retain data for a short window (days to weeks) for safety/abuse monitoring even after you opt out of training.
5. **For sensitive or client work**, use Incognito (Claude), Temporary Chat (ChatGPT), or disable activity history (Gemini) — or better, use a Team/Enterprise/API tier with a signed data agreement.

---

## Sources

- Anthropic Privacy Center — "Is my data used for model training?" (privacy.claude.com)
- Anthropic — "Updates to Consumer Terms and Privacy Policy" (anthropic.com/news)
- Anthropic — "Updates to our Privacy Policy" (privacy.anthropic.com)
- Privacy Watchdog by Terms.law — Anthropic and OpenAI policy reviews
- OpenAI Help Center — Data Controls documentation
- Google Cloud Documentation — Gemini Enterprise / Vertex AI data governance
- Various third-party trackers (Anonyome, Fello AI, MPG ONE, Predact, mePrism, Technerdo) — cross-checked for consistency as of mid-2026

*Disclaimer: This document summarizes publicly available information as of the verification date above and is not legal advice. Policies change; always confirm current terms directly with each provider before relying on them.*
