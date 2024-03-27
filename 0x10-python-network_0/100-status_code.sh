#!/bin/bash
# Check if URL is provided nas argument
curl -s -o /dev/null -w "%{http_code}" "$1"
