# Deployment Guide

This document outlines the steps required to deploy PepeTube on a RHEL-based system.

## Prerequisites

* RHEL or compatible distribution
* Sudo privileges

## Setup

1. Run the setup script to install system dependencies:

   ```bash
   ./deploy/rhel/setup.sh
   ```

2. Create a Python virtual environment and install application requirements.

   ```bash
   python3 -m venv /opt/pepetube/venv
   /opt/pepetube/venv/bin/pip install -r requirements.txt
   ```

## Gunicorn Service

1. Copy the provided systemd service file:

   ```bash
   sudo cp deploy/rhel/gunicorn.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable --now gunicorn
   ```

## Nginx Configuration

1. Copy the Nginx configuration:

   ```bash
   sudo cp deploy/rhel/nginx.conf /etc/nginx/conf.d/pepetube.conf
   sudo nginx -t
   sudo systemctl restart nginx
   ```

## Database Initialization

Configure PostgreSQL as needed, create the database and user for PepeTube.

## Application Deployment

1. Place the PepeTube source code in `/opt/pepetube`.
2. Ensure the `pepetube` user owns the application directory.
3. Restart the Gunicorn service after deploying new code:

   ```bash
   sudo systemctl restart gunicorn
   ```
