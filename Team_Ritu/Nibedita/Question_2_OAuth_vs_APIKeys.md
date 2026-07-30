Name: Nibedita
TASK
Date: July 29, 2026
Question 2: What is the main difference between OAuth and API Keys? Explain with
examples.
Both OAuth and API Keys are mechanism protocols used in web applications and API architectures to
manage access. However, they address fundamentally distinct requirements: Application Identification vs.
Delegated User Authorization.
1. API Keys (Application Identification)
An API Key is a unique string token passed by a client application to identify itself to an API service. It is
primarily used for identifying the calling project, tracking traffic metrics, and applying rate limits.
• Purpose: Identifies the requesting client application, not the end user.
• Security Level: Basic. A leaked API key allows unauthorized entities to impersonate the client until
revoked.
• Best Used For: Server-to-server calls, public datasets, internal microservices, or simple utility services.
Example: A web application requesting live weather data from an external API (such as OpenWeatherMap)
sends a static API key in the request header. The server checks the key to track application usage and enforce
quota limits.
2. OAuth (User Authorization & Delegated Access)
OAuth 2.0 is an authorization framework that enables third-party applications to obtain limited access to an
HTTP service on behalf of a resource owner (the user) without sharing the user's primary credentials.
• Purpose: Grants scoped access to specific user resources safely.
• Security Level: High. Utilizes short-lived access tokens, refresh tokens, and granular permissions.
• Best Used For: User login integrations ("Sign in with Google/GitHub") and granting applications access
to user accounts.
Example: Logging into a website using "Sign in with Google". Google requests user consent and issues a
temporary token to the website allowing access to basic user profile data without disclosing the Google
account password.
Key Comparison Summary
Feature API Keys OAuth 2.0
Primary Goal App Identification & Usage Tracking User Authorization & Scoped Access
Identifies The Calling Application The User (or App acting for User)
Security Basic (Static Secret) High (Tokens, Expiration, Scopes)

| Feature      | API Keys     | OAuth 2.0                      |
| ------------ | ------------ | ------------------------------ |
| User Consent | Not Required | Explicit User Consent Required |
Typical Use Case Public Data APIs / Analytics Social Logins / Cloud Storage Access
Submitted by Nibedita