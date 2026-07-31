# Day 04 - 29 July 2026

# Topic
OAuth Key (Dynamic & Session-Based) vs API Key (Static & Permanent)

## OAuth Key (Dynamic & Session-Based)

### Advantages
- More secure because access tokens expire automatically.
- Authenticates individual users before granting access.
- Supports fine-grained permissions using scopes.
- Refresh tokens allow secure renewal of expired access tokens.
- Users can revoke access without changing their passwords.

### Disadvantages
- More complex to implement than API keys.
- Requires OAuth server configuration and authentication flow.
- Access tokens expire, requiring token refresh handling.
- Higher development and maintenance effort.
- Depends on an authorization server for token issuance.

---

## API Key (Static & Permanent)

### Advantages
- Simple to generate and use.
- Easy and quick to integrate into applications.
- Ideal for server-to-server communication.
- No token refresh mechanism required.
- Lightweight authentication with minimal overhead.

### Disadvantages
- Less secure if the key is exposed.
- Does not authenticate individual users.
- Limited permission control compared to OAuth.
- Requires manual key rotation for security.
- Remains valid until manually revoked or regenerated.

---

# Comparison Table

| Feature                  | OAuth Key (Dynamic & Session-Based) | API Key (Static & Permanent)                       |
|--------------------------|-------------------------------------|----------------------------------------------------|
| **Security**             | High (short-lived tokens)           | Moderate (static key)                              |
| **Authentication**       | Authenticates users                 | Identifies the application only                    |
| **Token Validity**       | Temporary, expires automatically    | Permanent until revoked                            |
| **Permissions**          | Fine-grained access using scopes    | Usually broad or fixed access                      |
| **Implementation**       | Complex                             | Simple                                             |
| **Token Management**     | Requires refresh tokens             | No refresh required                                |
| **Best Use Case**        | User-facing applications,           | Internal APIs, server-to-server communication      |
| **Risk if Leaked**       | Limited due to token expiration     | High until the key is revoked                      |
| **Development Effort**   | Higher                              | Lower                                              |
| **Examples**             | Google Sign-In, GitHub OAuth, etc   | OpenAI API Key, Weather API Key, Stripe Secret Key |

---

## Summary

| OAuth Key                        | API Key                                               |
|----------------------------------|-------------------------------------------------------|
| Dynamic and session-based        | Static and permanent                                  |
| More secure                      | Easier to use                                         |
| User authentication              | Application authentication                            |
| Best for user-based applications | Best for backend services and simple API integrations |