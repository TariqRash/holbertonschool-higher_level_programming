#!/bin/bash
# Task 1: cURL API Consumption Examples
# Author: Tariq Rashed

echo "=========================================="
echo "Task 1: cURL API Consumption"
echo "=========================================="
echo ""

echo "1. Check curl version:"
curl --version
echo ""

echo "2. GET all posts:"
curl https://jsonplaceholder.typicode.com/posts
echo ""

echo "3. GET headers only:"
curl -I https://jsonplaceholder.typicode.com/posts
echo ""

echo "4. POST form data:"
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
echo ""

echo "5. POST JSON data:"
curl -X POST -H "Content-Type: application/json" -d '{"title":"foo","body":"bar","userId":1}' https://jsonplaceholder.typicode.com/posts
echo ""

echo "All examples completed!"
