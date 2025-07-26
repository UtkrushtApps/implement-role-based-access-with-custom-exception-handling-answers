# middleware.py
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        method = request.method
        path = request.url.path
        response = await call_next(request)
        status_code = response.status_code
        print(f"[RequestLog] {method} {path} -> {status_code}")
        return response
