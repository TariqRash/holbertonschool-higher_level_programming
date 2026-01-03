#!/bin/bash
# Task 1: cURL API Consumption Examples

echo "Task 1: cURL Examples"
echo "===================="

echo "1. Check curl version:"
curl --version

echo ""
echo "2. GET all posts:"
curl https://jsonplaceholder.typicode.com/posts

echo ""
echo "3. GET headers only:"
curl -I https://jsonplaceholder.typicode.com/posts

echo ""
echo "4. POST request:"
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

echo ""
echo "Completed!"
