# OAuth Key (Dynamic & Session-Based) vs API Key (Static & Permanent)

| | **OAuth Token** | **API Key** |
|---|---|---|
| Nature | Dynamic, short-lived, tied to a user/session, refreshed via a token flow | Static string, typically doesn't expire unless manually rotated |
| Identity | Represents a specific user with specific granted scopes | Represents an application/client, not an individual user |
| Revocation | User or admin can revoke access instantly, per-scope | Revoking means regenerating the key, which breaks every integration using it |
| Setup complexity | Higher — requires an auth server, redirect flow, token refresh logic | Low — generate a string, pass it in a header |

## OAuth — Positive

- **Least-privilege access**: tokens are scoped (e.g. "read calendar" but not "send email"), unlike an all-or-nothing key.
- **Short expiry limits blast radius**: a leaked access token is often useless within minutes/hours because it expires and must be refreshed.
- **Per-user revocation**: one compromised or offboarded user's access can be pulled without affecting anyone else.
- **Standardized, auditable flow**: widely implemented (Google, GitHub, Microsoft), well-understood security properties, supports MFA/consent screens.

## OAuth — Negative

- **Implementation overhead**: handling authorization codes, refresh tokens, and token storage/expiry correctly is easy to get wrong.
- **More moving parts to fail**: refresh bugs, clock skew, or misconfigured redirect URIs break auth in ways that are harder to debug than "the key is wrong."
- **Not ideal for pure server-to-server jobs** with no interactive user (client-credentials grant helps, but adds its own complexity).

## API Key — Positive

- **Trivial to integrate**: one static value in a header/query param; no flow to implement.
- **Good fit for server-to-server / machine-to-machine calls** where there's no user to consent.
- **Easy to reason about** for internal tools, scripts, and testing.

## API Key — Negative

- **Long-lived exposure risk**: if it leaks (committed to a repo, logged, exposed client-side), it typically stays valid until someone notices and manually rotates it.
- **No user-level identity**: can't tell which user or session performed an action, weakening audit trails.
- **Usually all-or-nothing permissions**, unless the provider layers its own scoping system on top.
- **Rotation is disruptive**: revoking one key breaks every consumer of it simultaneously — there's no per-session isolation.

## Takeaway

OAuth is the better default when a real user is involved and fine-grained, revocable access matters. API keys remain the pragmatic choice for simple service-to-service calls where the extra flow isn't worth the complexity — but they demand strict handling: environment variables/secret managers, never committed to source control, and rotated on a schedule.
