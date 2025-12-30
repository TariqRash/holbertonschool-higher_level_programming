#!/bin/bash
# Task 1: Consume data from an API using command line tools (curl)
# Author: Tariq Rashed
# Description: Demonstrates various curl commands for API interaction

echo "=========================================="
echo "Task 1: cURL API Consumption Examples"
echo "=========================================="
echo ""

# Check curl version
echo "1. Checking curl version:"
echo "Command: curl --version"
curl --version
echo ""
echo "=========================================="
echo ""

# Basic webpage fetch
echo "2. Fetching a basic webpage:"
echo "Command: curl http://example.com"
curl http://example.com
echo ""
echo "=========================================="
echo ""

# Fetch all posts from JSONPlaceholder
echo "3. Fetching all posts from JSONPlaceholder API:"
echo "Command: curl https://jsonplaceholder.typicode.com/posts"
curl https://jsonplaceholder.typicode.com/posts
echo ""
echo "=========================================="
echo ""

# Fetch only headers
echo "4. Fetching only headers (using -I flag):"
echo "Command: curl -I https://jsonplaceholder.typicode.com/posts"
curl -I https://jsonplaceholder.typicode.com/posts
echo ""
echo "=========================================="
echo ""

# Make a POST request
echo "5. Making a POST request to create a new post:"
echo "Command: curl -X POST -d \"title=foo&body=bar&userId=1\" https://jsonplaceholder.typicode.com/posts"
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
echo ""
echo "=========================================="
echo ""

# Fetch a single post with pretty JSON (if jq is available)
echo "6. Fetching a single post (ID: 1) with formatted JSON:"
echo "Command: curl https://jsonplaceholder.typicode.com/posts/1"
if command -v jq &> /dev/null; then
    echo "(Using jq for formatting)"
    curl https://jsonplaceholder.typicode.com/posts/1 | jq
else
    echo "(jq not installed - showing raw JSON)"
    curl https://jsonplaceholder.typicode.com/posts/1
fi
echo ""
echo "=========================================="
echo ""

# POST with JSON content type
echo "7. POST request with JSON content type:"
echo "Command: curl -X POST -H \"Content-Type: application/json\" -d '{\"title\":\"foo\",\"body\":\"bar\",\"userId\":1}' https://jsonplaceholder.typicode.com/posts"
curl -X POST -H "Content-Type: application/json" -d '{"title":"foo","body":"bar","userId":1}' https://jsonplaceholder.typicode.com/posts
echo ""
echo "=========================================="
echo ""

# PUT request to update a post
echo "8. PUT request to update a post (ID: 1):"
echo "Command: curl -X PUT -H \"Content-Type: application/json\" -d '{\"id\":1,\"title\":\"updated title\",\"body\":\"updated body\",\"userId\":1}' https://jsonplaceholder.typicode.com/posts/1"
curl -X PUT -H "Content-Type: application/json" -d '{"id":1,"title":"updated title","body":"updated body","userId":1}' https://jsonplaceholder.typicode.com/posts/1
echo ""
echo "=========================================="
echo ""

# DELETE request
echo "9. DELETE request to remove a post (ID: 1):"
echo "Command: curl -X DELETE https://jsonplaceholder.typicode.com/posts/1"
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
echo ""
echo "=========================================="
echo ""

# GET with query parameters
echo "10. GET request with query parameters (filter by userId):"
echo "Command: curl \"https://jsonplaceholder.typicode.com/posts?userId=1\""
curl "https://jsonplaceholder.typicode.com/posts?userId=1"
echo ""
echo "=========================================="
echo ""

echo "All curl examples completed!"
echo "=========================================="
