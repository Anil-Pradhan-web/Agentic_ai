# Clone SkillSpector
git clone https://github.com/NVIDIA/SkillSpector.git

cd SkillSpector

# Create environment
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Install
make install

# Verify
skillSpector --help


# Install OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash


# Install ClawHub skill
openclaw skills install @steipete/weather


# Find skill
find ~/.openclaw -name "SKILL.md"


# Scan skill
skillSpector scan --no-llm ~/.openclaw/workspace/skills/weather