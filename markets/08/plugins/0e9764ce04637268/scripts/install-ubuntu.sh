#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/opt/drop-dead-simple-ad-machine"

echo "Create application directory: ${APP_DIR}"
sudo mkdir -p "${APP_DIR}/knowledge"
sudo chown -R "$USER":"$USER" "${APP_DIR}"

echo
echo "Copy this project into ${APP_DIR}, then run:"
echo
echo "  cd ${APP_DIR}"
echo "  npm install"
echo "  cp .env.example .env"
echo "  sudo cp systemd/ad-machine.service /etc/systemd/system/"
echo "  sudo systemctl daemon-reload"
echo "  sudo systemctl enable --now ad-machine"
echo
echo "For HTTPS, configure nginx (nginx/ad-machine.conf, server_name mcp.mikeauton.com) and obtain a certificate with certbot."
