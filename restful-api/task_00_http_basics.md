# Task 0: Basics of HTTP/HTTPS

## HTTP vs HTTPS Core Differences

### HTTP (Hypertext Transfer Protocol)

**Characteristics:**
- Port: 80 (default)
- Security: No encryption
- Speed: Slightly faster (no encryption overhead)
- URL Format: http://example.com
- Use Case: Non-sensitive public information

**Security Concerns:**
- Data transmitted in plain text
- Vulnerable to man-in-the-middle attacks
- No data integrity verification
- Susceptible to eavesdropping
- Cannot verify server identity

---

### HTTPS (HTTP Secure)

**Characteristics:**
- Port: 443 (default)
- Security: SSL/TLS encryption
- Speed: Minimal overhead with modern hardware
- URL Format: https://example.com
- Use Case: Any website handling user data

**Security Benefits:**
- End-to-end encryption
- Data integrity verification
- Server authentication via certificates
- Protection against tampering
- SEO ranking boost (Google priority)

**How HTTPS Works:**
1. Client initiates connection (SSL/TLS handshake)
2. Server sends SSL certificate with public key
3. Client verifies certificate authenticity
4. Client encrypts session key with server public key
5. Server decrypts session key with private key
6. Encrypted communication begins using session key

---

## HTTP Request Structure

### Request Components
```
GET /api/users/123 HTTP/1.1
Host: api.example.com
User-Agent: Mozilla/5.0
Accept: application/json
Authorization: Bearer token123
Content-Type: application/json
```

**Components Breakdown:**
- Method: HTTP verb (GET, POST, PUT, DELETE)
- Path: Resource location (/api/users/123)
- Version: Protocol version (HTTP/1.1, HTTP/2)
- Host: Server domain (api.example.com)
- Headers: Metadata (Authorization, Content-Type)
- Body: Request payload (JSON, XML, form data)

---

## HTTP Response Structure

### Response Components
```
HTTP/1.1 200 OK
Date: Mon, 30 Dec 2024 14:30:00 GMT
Server: nginx/1.18.0
Content-Type: application/json
Content-Length: 348
Cache-Control: max-age=3600

{
    "id": 123,
    "name": "Tariq Rashed",
    "email": "tariq@hostworksa.com"
}
```

**Components Breakdown:**
- Status Line: Version + status code (HTTP/1.1 200 OK)
- Headers: Response metadata (Content-Type, Cache-Control)
- Body: Response payload (JSON, HTML, XML)

---

## Common HTTP Methods

### 1. GET
**Purpose:** Retrieve data from server  
**Properties:** Safe, Idempotent, Cacheable  
**Body:** No request body  
**Use Case:** Fetching user profiles, product listings, search results

**Example:**
```
GET /api/products?category=electronics&limit=10 HTTP/1.1
Host: api.store.com
```

---

### 2. POST
**Purpose:** Create new resources  
**Properties:** Not safe, Not idempotent  
**Body:** Contains data to create  
**Use Case:** User registration, creating blog posts, submitting forms

**Example:**
```
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "name": "Tariq Rashed",
    "email": "tariq@hostworksa.com"
}
```

---

### 3. PUT
**Purpose:** Update entire resource (full replacement)  
**Properties:** Idempotent  
**Body:** Complete resource representation  
**Use Case:** Updating user profiles, replacing configurations

**Example:**
```
PUT /api/users/456 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "name": "Tariq Rashed",
    "email": "newemail@hostworksa.com",
    "phone": "+966501234567"
}
```

---

### 4. DELETE
**Purpose:** Remove resources  
**Properties:** Idempotent  
**Body:** Usually empty  
**Use Case:** Deleting user accounts, removing posts

**Example:**
```
DELETE /api/users/456 HTTP/1.1
Host: api.example.com
Authorization: Bearer token123
```

---

### 5. PATCH
**Purpose:** Partial resource updates  
**Properties:** Not necessarily idempotent  
**Body:** Only fields to update  
**Use Case:** Updating single fields, toggling status

**Example:**
```
PATCH /api/users/456 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "phone": "+966501234567"
}
```

---

## HTTP Status Codes

### 2xx Success

**200 OK**
- Description: Request succeeded
- Scenario: Successful GET request

**201 Created**
- Description: Resource created successfully
- Scenario: User registration complete

**204 No Content**
- Description: Success but no content to return
- Scenario: Successful DELETE operation

---

### 3xx Redirection

**301 Moved Permanently**
- Description: Resource permanently moved
- Scenario: Domain change, URL restructure

**302 Found**
- Description: Temporary redirect
- Scenario: Maintenance page

**304 Not Modified**
- Description: Resource has not changed
- Scenario: Browser cache validation

---

### 4xx Client Errors

**400 Bad Request**
- Description: Malformed request syntax
- Scenario: Invalid JSON, missing required fields

**401 Unauthorized**
- Description: Authentication required
- Scenario: Missing or invalid credentials

**403 Forbidden**
- Description: Server refuses request
- Scenario: Insufficient permissions

**404 Not Found**
- Description: Resource does not exist
- Scenario: Requesting non-existent user ID

**429 Too Many Requests**
- Description: Rate limit exceeded
- Scenario: API throttling, DDoS protection

---

### 5xx Server Errors

**500 Internal Server Error**
- Description: Generic server error
- Scenario: Unhandled exception, bug

**502 Bad Gateway**
- Description: Invalid response from upstream
- Scenario: Proxy or gateway error

**503 Service Unavailable**
- Description: Server overloaded or maintenance
- Scenario: Scheduled downtime

**504 Gateway Timeout**
- Description: Upstream server timeout
- Scenario: Slow database query

---

## Security Comparison: Real-World Example

### Banking Website Scenario

**HTTP (Insecure):**
```
User enters password: "MyPassword123"
Transmitted as: "MyPassword123" (plain text)
Attacker on network: Can see password directly
Result: Account compromised
```

**HTTPS (Secure):**
```
User enters password: "MyPassword123"
Transmitted as: "k3jH9f2lP0qR8..." (encrypted)
Attacker on network: Sees encrypted gibberish
Result: Account secure
```

---

## Summary

### Key Takeaways

- HTTPS equals HTTP plus encryption - Always use for sensitive data
- Status codes matter - They communicate operation results
- Methods have purpose - Use correct verb for each operation
- Headers carry metadata - Authentication, content types, caching
- RESTful design - Stateless, resource-based, uniform interface

### Best Practices

1. Always use HTTPS for production applications
2. Return appropriate status codes for each scenario
3. Use correct HTTP methods (do not use GET to delete)
4. Include descriptive error messages in response bodies
5. Implement proper authentication and authorization
6. Cache appropriately to reduce server load
7. Version your APIs for backward compatibility

---

## Testing HTTP Requests with cURL
```bash
# GET request
curl -X GET https://api.example.com/users/123

# POST request
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Tariq","email":"tariq@hostworksa.com"}'

# PUT request
curl -X PUT https://api.example.com/users/123 \
  -H "Authorization: Bearer token123" \
  -d '{"name":"Updated Name"}'

# DELETE request
curl -X DELETE https://api.example.com/users/123 \
  -H "Authorization: Bearer token123"
```

---

**Author:** Tariq Rashed  
**Date:** December 30, 2024  
**Project:** RESTful API - HTTP/HTTPS Fundamentals
