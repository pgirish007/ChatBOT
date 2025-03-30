#!/bin/bash

# Prompt for username and password
read -p "Enter Username: " username
read -s -p "Enter Password: " password
echo

# Send request using curl
curl -u "$username:$password" -X POST http://127.0.0.1:5000/chatbot \
     -H "Content-Type: application/json" \
     -d '{"user_id": "123", "message": "I want to build"}'

