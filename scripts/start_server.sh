#!/bin/bash
set -e
echo "Starting application..."
cd /home/ubuntu/app
nohup python3 app.py > /var/log/app.log 2>&1 &
echo "Application started on port 8080!"
