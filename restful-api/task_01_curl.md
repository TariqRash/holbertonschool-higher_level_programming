# Task 1: Consume Data from API using cURL

## What is cURL

cURL is a command-line tool for transferring data with URLs. It supports HTTP, HTTPS, FTP, and many other protocols.

## Installation

### Linux
```bash
sudo apt-get install curl
```

### Verify
```bash
curl --version
```

## Basic Examples

### Example 1: GET Request
```bash
curl https://jsonplaceholder.typicode.com/posts
```

**Description:** Fetches all posts

**Expected Output:** JSON array of posts

### Example 2: Headers Only
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

**Description:** Fetches only HTTP headers

**Expected Output:**
```
HTTP/2 200
content-type: application/json
```

### Example 3: POST Form Data
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

**Description:** Creates a new post with form data

**Expected Output:**
```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

### Example 4: POST JSON Data
```bash
curl -X POST -H "Content-Type: application/json" -d '{"title":"foo","body":"bar","userId":1}' https://jsonplaceholder.typicode.com/posts
```

**Description:** Creates a post with JSON payload

**Expected Output:**
```json
{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}
```

### Example 5: GET Single Resource
```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

**Expected Output:**
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere...",
  "body": "quia et suscipit..."
}
```

### Example 6: PUT Request
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"id":1,"title":"updated","body":"updated","userId":1}' https://jsonplaceholder.typicode.com/posts/1
```

**Description:** Updates entire resource

### Example 7: DELETE Request
```bash
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

**Description:** Deletes a resource

**Expected Output:** Empty object or success status

### Example 8: Query Parameters
```bash
curl "https://jsonplaceholder.typicode.com/posts?userId=1"
```

**Description:** Filters posts by userId

## Common cURL Options

| Option | Description |
|--------|-------------|
| -X | HTTP method (GET, POST, PUT, DELETE) |
| -H | Add header |
| -d | Send data |
| -I | Headers only |
| -i | Include headers in output |
| -o | Save to file |
| -v | Verbose mode |

## Authentication Examples

### Bearer Token
```bash
curl -H "Authorization: Bearer TOKEN" https://api.example.com/data
```

### Basic Auth
```bash
curl -u username:password https://api.example.com/data
```

### API Key
```bash
curl -H "X-API-Key: your_key" https://api.example.com/data
```

## JSON Formatting with jq

Install jq:
```bash
sudo apt-get install jq
```

Usage:
```bash
curl https://jsonplaceholder.typicode.com/posts/1 | jq
```

## Summary

Key takeaways:
- cURL is essential for API testing
- Use -X to specify HTTP method
- Use -H for headers
- Use -d for data payload
- Use -I for headers only

## Resources

- [cURL Documentation](https://curl.se/docs/)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)

**Author:** Tariq Rashed  
**Date:** December 30, 2024
