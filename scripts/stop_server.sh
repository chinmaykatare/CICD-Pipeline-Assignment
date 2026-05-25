#!/bin/bash
echo "Stopping application..."
pkill -f "python3 app.py" || true
echo "Application stopped!"
