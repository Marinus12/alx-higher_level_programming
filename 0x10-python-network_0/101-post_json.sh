#!/bin/bash
# Sends a JSON POST request to URL passed as the argument as the first argument
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
