#!/usr/bin/env bash
set -euo pipefail

# Update system packages
sudo dnf -y update

# Install Python, PostgreSQL and Nginx
sudo dnf -y install \
    python3 python3-virtualenv python3-pip \
    postgresql-server postgresql-contrib \
    nginx

# Initialize PostgreSQL if not already initialized
if [ ! -d /var/lib/pgsql/data/base ]; then
    sudo postgresql-setup --initdb --unit postgresql
fi

# Enable and start services
sudo systemctl enable --now postgresql
sudo systemctl enable --now nginx

# Open firewall for HTTP/HTTPS if firewalld is present
if systemctl is-active --quiet firewalld; then
    sudo firewall-cmd --permanent --add-service=http
    sudo firewall-cmd --permanent --add-service=https
    sudo firewall-cmd --reload
fi
