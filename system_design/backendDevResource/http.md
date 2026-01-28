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
-               Request                                     Response
1. Method: get, put                                        http/1.1 200 ok
2. Host : example.com (Server domain)                      Date:
3. User-agent : browser Name                               Content-type: application/json
4. Content-type: Application/json(Format of request body)                          
5. Content-length: 123                                     Content-length: 123
6. Authorisation: Bearer djsbdbsjdsdj                      Serevr:Apache/2.2.3 (ubuntu)
7. Accept: application/json                                Cache-Control: no-store
8. Accept-Encoding: gzip, deflate,br                       X-Request-ID: abcdef12345
9. Connection: keep-alive                                  Strict-Transport-Security:max-age=310202 
10. Referer: Https/example.con/dashboard                   includeSubDomains:preload
11. Cookies: sessionId=abshsbsjsj ; lang=en-us             Set-Cookies:sessionID=abcd123, path=/,secure;HttpOnly
                                                           Vary:Accept-Encoding
                                                           Conection:Keep-alive

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