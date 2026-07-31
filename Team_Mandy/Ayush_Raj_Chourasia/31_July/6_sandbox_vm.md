# Sandbox Setup / Virtual Machine for Agentic AI

When developing and running Autonomous AI Agents (like AutoGPT, OpenHands, or custom OpenClaw agents), safety is the highest priority. Because agents can write code, execute bash commands, and delete files autonomously, running them on your primary host operating system is extremely dangerous. 

**Rule #1 of Agentic AI:** Never run an agent on your host machine. Always use a sandbox.

## 1. Why a Virtual Machine (VM)?
While Docker containers offer some isolation, a Virtual Machine provides a full hardware-level virtualization layer. If an agent goes rogue (e.g., hallucinating an `rm -rf /` command or downloading malware while browsing the web), it will only destroy the disposable VM, keeping your personal files, SSH keys, and system registry safe.

## 2. Setup Guide using VirtualBox (Local)
1. **Download VirtualBox:** Install Oracle VirtualBox for your OS.
2. **Download an OS Image:** Download a lightweight Linux distribution ISO, such as Ubuntu Server or Debian.
3. **Create the VM:**
   - Allocate at least 4GB of RAM and 2 CPUs.
   - Create a dynamic Virtual Hard Disk (approx 20GB).
4. **Network Settings:** Set the networking to NAT. This gives the agent internet access but prevents it from easily scanning or attacking your local home network (unlike Bridged mode).
5. **Install the OS:** Boot the ISO, run through the basic Linux installation, and install `git`, `python3`, and `pip`.

## 3. Best Practices for the VM
- **No Secrets:** Do not put your personal AWS keys, GitHub tokens, or passwords inside the VM. Only provide the agent with highly restricted, scoped API keys specifically generated for its task.
- **Snapshots:** Before you launch a new agent run, take a Snapshot of the VM state in VirtualBox. If the agent corrupts the environment, you can restore the clean snapshot in 5 seconds.
- **Monitoring:** Open a terminal to watch the agent's actions (e.g., via `htop` or tailing logs) so you can pull the plug (shut down the VM) if it starts behaving unexpectedly.
