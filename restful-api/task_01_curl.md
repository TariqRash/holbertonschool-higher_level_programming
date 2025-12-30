# Task 1: Consume Data from an API using cURL

## 📡 What is cURL?

**cURL (Client URL)** is a command-line tool for transferring data with URLs. It supports numerous protocols including HTTP, HTTPS, FTP, SFTP, and more. cURL is essential for:
- API testing and debugging
- Automated data retrieval
- Server diagnostics
- Webhook testing
- CI/CD pipelines

---

## 🎯 Learning Objectives

By completing this task, you will:
1. ✅ Install and verify cURL installation
2. ✅ Execute basic HTTP requests from command line
3. ✅ Understand HTTP methods (GET, POST, PUT, DELETE)
4. ✅ Work with request headers and data payloads
5. ✅ Interpret API responses and status codes

---

## 🔧 Installation

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install curl
```

### macOS
```bash
# Usually pre-installed
# If not, use Homebrew:
brew install curl
```

### Windows
```bash
# Use Windows Subsystem for Linux (WSL)
# Or download from: https://curl.se/windows/
```

### Verify Installation
```bash
curl --version
```

**Expected Output:**
```
curl 7.68.0 (x86_64-pc-linux-gnu)
Release-Date: 2020-01-08
Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3...
Features: AsynchDNS GSS-API HTTP2 HTTPS-proxy IPv6 Kerberos Largefile...
```

---

## 📚 Basic cURL Syntax
```bash
curl [options] [URL]
```

### Common Options

| Option | Description | Example |
|--------|-------------|---------|
| `-X` | Specify HTTP method | `-X POST` |
| `-H` | Add custom header | `-H "Content-Type: application/json"` |
| `-d` | Send data in request body | `-d '{"key":"value"}'` |
| `-I` | Fetch headers only | `-I` |
| `-o` | Save output to file | `-o output.json` |
| `-i` | Include response headers | `-i` |
| `-v` | Verbose output | `-v` |
| `-s` | Silent mode | `-s` |

---

## 🌐 Task Examples with JSONPlaceholder API

### Example 1: Basic GET Request

**Command:**
```bash
curl https://jsonplaceholder.typicode.com/posts
```

**Description:** Fetches all posts from the API

**Expected Output:**
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident...",
    "body": "quia et suscipit..."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae..."
  }
  ...
]
```

---

### Example 2: Fetch Headers Only

**Command:**
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

**Description:** Retrieves only HTTP headers without the response body

**Expected Output:**
```
HTTP/2 200
date: Mon, 30 Dec 2024 15:00:00 GMT
content-type: application/json; charset=utf-8
content-length: 27707
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
cache-control: max-age=43200
expires: Mon, 30 Dec 2024 03:00:00 GMT
```

**Analysis:**
- ✅ Status: 200 (Success)
- ✅ Content-Type: JSON
- ✅ Rate Limit: 1000 requests
- ✅ Cache: Valid for 12 hours

---

### Example 3: GET Single Resource

**Command:**
```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

**Description:** Fetches a specific post by ID

**Expected Output:**
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

---

### Example 4: POST Request (Form Data)

**Command:**
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

**Description:** Creates a new post using form-encoded data

**Expected Output:**
```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

**Note:** JSONPlaceholder simulates creation and returns ID 101

---

### Example 5: POST Request (JSON Data)

**Command:**
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"My Post","body":"This is my post content","userId":1}' \
  https://jsonplaceholder.typicode.com/posts
```

**Description:** Creates a new post using JSON payload

**Expected Output:**
```json
{
  "title": "My Post",
  "body": "This is my post content",
  "userId": 1,
  "id": 101
}
```

---

### Example 6: PUT Request (Update Resource)

**Command:**
```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"id":1,"title":"Updated Title","body":"Updated Body","userId":1}' \
  https://jsonplaceholder.typicode.com/posts/1
```

**Description:** Updates an entire resource (full replacement)

**Expected Output:**
```json
{
  "id": 1,
  "title": "Updated Title",
  "body": "Updated Body",
  "userId": 1
}
```

---

### Example 7: PATCH Request (Partial Update)

**Command:**
```bash
curl -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"title":"Partially Updated Title"}' \
  https://jsonplaceholder.typicode.com/posts/1
```

**Description:** Updates only specified fields

**Expected Output:**
```json
{
  "userId": 1,
  "id": 1,
  "title": "Partially Updated Title",
  "body": "quia et suscipit..."
}
```

---

### Example 8: DELETE Request

**Command:**
```bash
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

**Description:** Deletes a resource

**Expected Output:**
```json
{}
```

**Status Code:** 200 (JSONPlaceholder returns empty object)

---

### Example 9: Query Parameters

**Command:**
```bash
curl "https://jsonplaceholder.typicode.com/posts?userId=1"
```

**Description:** Filters posts by userId

**Expected Output:** Array of posts where userId equals 1

---

### Example 10: Multiple Query Parameters

**Command:**
```bash
curl "https://jsonplaceholder.typicode.com/comments?postId=1&_limit=5"
```

**Description:** Fetches 5 comments for post ID 1

---

## 🎨 Formatting JSON Output with jq

**Install jq:**
```bash
# Ubuntu/Debian
sudo apt-get install jq

# macOS
brew install jq
```

**Usage:**
```bash
curl https://jsonplaceholder.typicode.com/posts/1 | jq
```

**Output:**
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat...",
  "body": "quia et suscipit..."
}
```

**Extract specific field:**
```bash
curl https://jsonplaceholder.typicode.com/posts/1 | jq '.title'
```

**Output:**
```
"sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
```

---

## 🔐 Authentication Examples

### Basic Authentication
```bash
curl -u username:password https://api.example.com/data
```

### Bearer Token
```bash
curl -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  https://api.example.com/protected
```

### API Key (Header)
```bash
curl -H "X-API-Key: your_api_key_here" \
  https://api.example.com/data
```

### API Key (Query Parameter)
```bash
curl "https://api.example.com/data?api_key=your_api_key_here"
```

---

## 📊 Advanced cURL Techniques

### Save Response to File
```bash
curl https://jsonplaceholder.typicode.com/posts/1 -o post.json
```

### Include Response Headers in Output
```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

### Follow Redirects
```bash
curl -L https://bit.ly/shortened-url
```

### Set Custom User-Agent
```bash
curl -A "MyApp/1.0" https://api.example.com/data
```

### Verbose Output (Debugging)
```bash
curl -v https://jsonplaceholder.typicode.com/posts/1
```

### Silent Mode (No Progress)
```bash
curl -s https://jsonplaceholder.typicode.com/posts/1
```

### Set Timeout
```bash
curl --max-time 30 https://api.example.com/slow-endpoint
```

---

## 🧪 Practical Exercises

### Exercise 1: Fetch All Users
```bash
curl https://jsonplaceholder.typicode.com/users
```

**Task:** Count how many users are returned

---

### Exercise 2: Create a Comment
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"postId":1,"name":"Tariq","email":"tariq@hostworksa.com","body":"Great post!"}' \
  https://jsonplaceholder.typicode.com/comments
```

**Task:** Verify the response includes an ID

---

### Exercise 3: Update User Information
```bash
curl -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"name":"Tariq Rashed"}' \
  https://jsonplaceholder.typicode.com/users/1
```

**Task:** Confirm the name was updated

---

### Exercise 4: Fetch Nested Resources
```bash
curl https://jsonplaceholder.typicode.com/posts/1/comments
```

**Task:** List all comments for post ID 1

---

## 🎯 Real-World Use Cases

### 1. API Health Check
```bash
#!/bin/bash
response=$(curl -s -o /dev/null -w "%{http_code}" https://api.example.com/health)
if [ $response -eq 200 ]; then
    echo "API is healthy"
else
    echo "API is down (Status: $response)"
fi
```

### 2. Automated Data Backup
```bash
#!/bin/bash
curl https://api.example.com/data/export > backup_$(date +%Y%m%d).json
```

### 3. Webhook Testing
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"event":"user.created","data":{"id":123}}' \
  https://webhook.example.com/endpoint
```

---

## 📝 Summary

### Key Takeaways

✅ **cURL is powerful** - Command-line API interaction  
✅ **HTTP methods matter** - GET, POST, PUT, PATCH, DELETE  
✅ **Headers are essential** - Content-Type, Authorization  
✅ **Data formats vary** - Form-encoded vs JSON  
✅ **Testing is easy** - No GUI needed for API testing

### Best Practices

1. **Always specify Content-Type** for POST/PUT requests
2. **Use -i or -v** for debugging
3. **Pipe to jq** for readable JSON
4. **Save responses** to files for analysis
5. **Handle authentication** properly (never hardcode tokens)
6. **Check status codes** before processing responses

---

## 🔗 Resources

- [cURL Official Documentation](https://curl.se/docs/)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)
- [HTTP Status Codes](https://httpstatuses.com/)
- [jq Manual](https://stedolan.github.io/jq/manual/)

---

**Author:** Tariq Rashed  
**Date:** December 30, 2024  
**Project:** RESTful API - cURL API Consumption
