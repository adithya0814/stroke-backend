#!/usr/bin/env bash
# exit on error
set -o errexit

# Install system dependencies for OpenCV/MediaPipe
apt-get update && apt-get install -y libgl1

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
