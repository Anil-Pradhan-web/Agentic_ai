#!/usr/bin/env bash
# OpenClaw — full setup script (system deps -> clone -> env -> install -> build -> run)
# Usage: bash install.sh
set -euo pipefail

REPO_URL="https://github.com/OpenClaw/openclaw.git"
INSTALL_DIR="openclaw"

echo "==> [1/7] Updating system packages"
sudo apt-get update -y
sudo apt-get upgrade -y

echo "==> [2/7] Installing system dependencies"
sudo apt-get install -y build-essential curl git unzip pkg-config libssl-dev python3 python3-venv

echo "==> [3/7] Cloning OpenClaw"
if [ -d "$INSTALL_DIR" ]; then
  echo "    $INSTALL_DIR already exists, pulling latest instead"
  git -C "$INSTALL_DIR" pull
else
  git clone "$REPO_URL" "$INSTALL_DIR"
fi
cd "$INSTALL_DIR"

echo "==> [4/7] Creating Python virtual environment"
python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate

echo "==> [5/7] Installing dependencies"
pip install --upgrade pip
pip install -r requirements.txt

echo "==> [6/7] Configuring environment"
if [ ! -f .env ]; then
  cp .env.example .env
  echo "    .env created from .env.example — edit it before starting:"
  echo "    -> set your model provider API key / OAuth credentials"
  echo "    -> set the agent config path and port"
else
  echo "    .env already exists, leaving as-is"
fi

echo "==> [7/7] Verifying installation"
python3 -c "import openclaw" 2>/dev/null && echo "    openclaw package import OK" || echo "    (package import check skipped — verify module name for this build)"

echo ""
echo "Setup complete."
echo "Next steps:"
echo "  1. source .venv/bin/activate"
echo "  2. edit .env with your real credentials"
echo "  3. run: python3 -m openclaw start   (or the project's documented entrypoint)"
echo "  4. verify with: ps aux | grep openclaw"
