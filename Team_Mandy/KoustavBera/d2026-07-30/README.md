# 🦞 Installing OpenClaw on Fedora 44 (The Smooth Way)

> A guide for Fedora users who want to try OpenClaw without breaking their existing Node.js installation.

I recently installed OpenClaw on **Fedora 44** and ran into several issues that aren't obvious from the official installation guide. This guide documents the cleanest approach I found after debugging everything.

---

## ⚠️ The Problem

If you're using Fedora 44, chances are you already have Fedora's official Node.js packages installed.

For example:

```bash
node -v
# v22.22.2

rpm -qa | grep nodejs
```

You'll likely see packages similar to:

```
nodejs22
nodejs22-bin
nodejs22-npm
nodejs22-libs
...
```

If you follow the default installer:

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

it may try to install **NodeSource Node.js**, which conflicts with Fedora's packages.

Example error:

```
file /usr/bin/node conflicts with package nodejs22-bin
file /usr/bin/npm conflicts with package nodejs22-npm-bin
```

This is **not** a Fedora bug.

Fedora packages Node differently than NodeSource, and both packages own the same binaries.

---

# ✅ The Correct Installation Method

Instead of using the default installer, use the **local prefix installer**.

```bash
curl -fsSL https://openclaw.ai/install-cli.sh | bash
```

This installs everything under:

```
~/.openclaw
```

It **does not**

- replace Fedora's Node
- install NodeSource
- modify `/usr/bin/node`
- interfere with your existing development setup

It simply bundles its own supported Node runtime.

---

# Add OpenClaw to PATH

After installation I got:

```
openclaw: command not found
```

The binary was actually installed at

```
~/.openclaw/bin/openclaw
```

Simply add it to your PATH:

```bash
echo 'export PATH="$HOME/.openclaw/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

If you use Bash:

```bash
echo 'export PATH="$HOME/.openclaw/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Verify:

```bash
which openclaw
```

Expected output:

```
~/.openclaw/bin/openclaw
```

---

# Verify Installation

```bash
openclaw --version
```

Example:

```
OpenClaw 2026.7.1-2
```

---

# Claude CLI Integration

If you're using **Claude Pro / Max** via Claude Code (recommended):

Install Claude Code first.

Verify:

```bash
which claude
claude --version
```

Then authenticate:

```bash
claude auth login
```

Connect OpenClaw to Claude:

```bash
openclaw models auth login --provider anthropic
```

Restart the gateway:

```bash
openclaw gateway restart
```

Check everything:

```bash
openclaw doctor
```

You should see something like:

```
Binary: /usr/bin/claude
Headless Claude auth: OK
```

---

# Common Errors

## ❌ NodeSource conflicts

```
file /usr/bin/node conflicts with package nodejs22-bin
```

**Don't remove Fedora's Node packages.**

Use:

```bash
install-cli.sh
```

instead.

---

## ❌ openclaw: command not found

OpenClaw was installed correctly.

Add

```
~/.openclaw/bin
```

to your PATH.

---

## ❌ write EPIPE

Run:

```bash
openclaw doctor
```

In my case the cause was:

```
Binary: command "claude" was not found
```

Installing Claude Code fixed the issue.

---

# Stopping the Gateway

OpenClaw installs a **systemd user service**.

Stop it:

```bash
openclaw gateway stop
```

Start it again:

```bash
openclaw gateway start
```

Restart:

```bash
openclaw gateway restart
```

---

# Does OpenClaw Replace My System Node?

**No.**

My system still uses:

```bash
node -v
```

```
v22.22.2
```

OpenClaw uses its own runtime:

```
~/.openclaw/tools/node-v24.x/
```

My Fedora installation remains untouched.

---

# Where is OpenClaw Installed?

Everything lives under:

```
~/.openclaw
```

Useful locations:

```
~/.openclaw/
├── bin/
├── tools/
├── workspace/
├── openclaw.json
└── ...
```

---

# My Thoughts

After spending a few hours with OpenClaw:

### Things I liked

- Clean installation using the local installer.
- Doesn't interfere with Fedora packages.
- Excellent terminal UI.
- Claude CLI integration is seamless.
- Highly customizable personality.

### Things to know

OpenClaw is **not** a replacement for:

- ChatGPT
- Claude Code
- Codex

Instead, think of it as an **AI operating system** or **automation layer**.

Its biggest strength is:

- persistent memory
- automation
- scheduling
- cross-device workflows
- background agents

If you're only looking for a coding assistant, **Claude Code is probably enough**.

If you want a long-running AI assistant that can automate your workflow and remember context across sessions, OpenClaw starts to shine.

---

# Fedora Verdict

⭐⭐⭐⭐☆

The default installer currently doesn't play nicely with Fedora's Node packaging, but the **local installer works perfectly**.

Once installed, OpenClaw feels right at home on Fedora.

Happy hacking! 🐧
