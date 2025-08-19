#!/usr/bin/env bash
# setup.sh - Install dependencies for Gradescope autograder

apt-get update
apt-get install -y python3 python3-pip
pip3 install --upgrade pip
