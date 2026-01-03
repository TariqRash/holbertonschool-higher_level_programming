# Task 0: Basics of HTTP/HTTPS

## HTTP vs HTTPS Differences

### HTTP (Hypertext Transfer Protocol)
- Port: 80
- Security: No encryption
- Data: Plain text transmission
- Use: Public, non-sensitive content

### HTTPS (HTTP Secure)
- Port: 443
- Security: SSL/TLS encryption
- Data: Encrypted transmission
- Use: Sensitive data, authentication

## HTTP Request Structure
```
GET /api/users HTTP/1.1
Host: api.example.com
User-Agent: Mozilla/5.0
Accept: application/json
Authorization: Bearer token
```

## HTTP Response Structure
```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{"status": "success"}
```

## Common HTTP Methods

1. **GET** - Retrieve data
2. **POST** - Create new resources
3. **PUT** - Update entire resource
4. **PATCH** - Partial update
5. **DELETE** - Remove resource

## HTTP Status Codes

### 2xx Success
- 200 OK - Request successful
- 201 Created - Resource created
- 204 No Content - Success, no data

### 3xx Redirection
- 301 Moved Permanently - URL changed
- 302 Found - Temporary redirect
- 304 Not Modified - Cached version valid

### 4xx Client Errors
- 400 Bad Request - Invalid syntax
- 401 Unauthorized - Authentication required
- 403 Forbidden - Access denied
- 404 Not Found - Resource not found
- 429 Too Many Requests - Rate limited

### 5xx Server Errors
- 500 Internal Server Error - Server error
- 502 Bad Gateway - Invalid response
- 503 Service Unavailable - Server down
- 504 Gateway Timeout - Request timeout

**Author:** Tariq Rashed
