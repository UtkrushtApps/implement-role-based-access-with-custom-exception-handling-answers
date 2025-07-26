# main.py
from fastapi import FastAPI
from middleware import RequestLoggingMiddleware
from routers import orders
import uvicorn

app = FastAPI(
    title="E-Commerce Order API",
    version="1.0.0"
)

app.add_middleware(RequestLoggingMiddleware)

app.include_router(orders.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
