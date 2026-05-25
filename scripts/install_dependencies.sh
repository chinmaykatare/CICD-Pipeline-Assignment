#!/bin/bash
set -e
echo "Updating packages..."
apt-get update -y
echo "Installing Python..."
apt-get install -y python3 python3-pip
echo "Installing app dependencies..."
cd /home/ubuntu/app
pip3 install -r requirements.txt
echo "Dependencies installed!"
