# understanding of HTTP 
- medium through client talk to servers or send req, get res.
- HTPP is      
1.Stateless: 
- server doesnt have past req , o tarck  session 
- to maintain the state developer uses cookies , token, session , localStorage method etc.
- Every request is treated as new and independent
2.Client server Model:
- HTTP works on a strict client–server architecture:
- Client : initiate the communicatin
- Server :  responds (never initiates communication)

# HTTP Request V/s HTTP Response


# 📌 Comparison Table

| **HTTP Request**                                      | **HTTP Response** |
|-------------------------------------------------------|-------------------|
| **Method:** GET, POST, PUT                            | **Status Line:** `HTTP/1.1 200 OK` |
| **Host:** example.com (Server domain)                 | **Date:** `<server-date>` |
| **User-Agent:** Browser name                          | **Content-Type:** application/json |
| **Content-Type:** application/json (request body format) | **Content-Length:** 123 |
| **Content-Length:** 123                               | **Server:** Apache/2.2.3 (Ubuntu) |
| **Authorization:** Bearer djsbdbsjdsdj                | **Cache-Control:** no-store |
| **Accept:** application/json                          | **X-Request-ID:** abcdef12345 |
| **Accept-Encoding:** gzip, deflate, br                | **Strict-Transport-Security:** max-age=310202; includeSubDomains; preload |
| **Connection:** keep-alive                            | **Set-Cookie:** sessionID=abcd123; Path=/; Secure; HttpOnly |
| **Referer:** https://example.com/dashboard            | **Vary:** Accept-Encoding |
| **Cookies:** sessionId=abshsbsjsj; lang=en-us         | **Connection:** keep-alive |




// Request Body:                                           Response Body:
{                                                          {
    "firstName":"ankan",                                    "message": "user added successfully,
    "email":"ankan@gmail.com",                               " UserId": 123
    "age":30                                                 "status":"success"

}                                                          }

# Type of HTTP 
# Request Header
1. User-Agent: Browser friendly 
2. Authentication
3. Cookies: setting token here, info
4. Accept: formate of response body(application/josn) kong of infomation client expect from sever to accept

# General- Header
1. Date
2. Cache-Control
3. Connection:keep alive
#