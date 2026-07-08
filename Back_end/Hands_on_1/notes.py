"""
=========================================================
TASK 1
WEB FRAMEWORK FOUNDATIONS
=========================================================

1. Request-Response Cycle

Browser
   |
   | GET /api/courses/
   |
URL Router (urls.py)
   |
View (views.py)
   |
Model (models.py)
   |
Database Query
   |
Model returns data
   |
View processes data
   |
HttpResponse / JsonResponse
   |
Browser


2. Middleware

Middleware sits between the request and the view.

Incoming Request

Browser
    |
Middleware
    |
URL Routing
    |
View
    |
Response
    |
Middleware
    |
Browser

Examples:

SecurityMiddleware
- Adds security headers.
- Protects against common attacks.

SessionMiddleware
- Handles user sessions.
- Stores session data.


3. WSGI vs ASGI

WSGI
-----
- Web Server Gateway Interface
- Handles synchronous requests.
- One request is processed at a time.

ASGI
-----
- Asynchronous Server Gateway Interface
- Supports async programming.
- Handles WebSockets.
- Supports long-lived connections.

Django uses WSGI by default.

Switch to ASGI when:
- Building chat applications
- Real-time notifications
- WebSockets
- High concurrency applications


4. MVC vs MVT

MVC

Model
View
Controller

Django follows MVT

Model
- Database

View
- Business logic
- Equivalent to Controller in MVC

Template
- HTML Presentation
- Equivalent to View in MVC

Mapping

MVC Model      -> Django Model

MVC View       -> Django Template

MVC Controller -> Django View
"""