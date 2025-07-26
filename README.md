1. **Create the Router for Orders:**
   - In `routers/orders.py`, define an API router for order operations (prefix `/orders`).
   - Use a Pydantic model (`OrderCreate`) for POST input validation.
   - Move the order endpoint implementation to this router, and use `BackgroundTasks` to offload the `notify_staff` function (simulates slow staff notification).

2. **Add a Middleware for Request Logging:**
   - In `middleware.py`, create a subclass of `BaseHTTPMiddleware`.
   - Override the `dispatch` method to log the HTTP method, path, and status code of every request/response to stdout.

3. **Wire Up Main Application:**
   - In `main.py`, instantiate FastAPI, register the custom logging middleware and the order router from `routers.orders` using `include_router`.
   - Ensure the application has a proper entry point for running with Uvicorn (suitable for both local and Docker usage).

4. **Make Routers Importable:**
   - In `routers/__init__.py`, make sure the directory is recognized as a package (an empty file suffices).

5. **Write a Dockerfile for Containerization:**
   - Use `python:3.11-slim` as a modern base image.
   - Copy the source code and install only the required dependencies (FastAPI and Uvicorn).
   - Expose port 8000 and set the default CMD to run Uvicorn with the app.

6. **Best Practices Followed:**
   - Separation of concerns (routers, middleware, main app setup).
   - Use of BackgroundTasks for non-blocking long-running operations.
   - Pydantic validation for input.
   - Container-ready application structure.

7. **How It Works:**
   - When a POST is made to `/orders/`, the API immediately responds with a success message (HTTP 201), even though the notification takes 2 seconds simulated delay.
   - Middleware logs each HTTP request's method, path, and status code to stdout.
   - The project can be built and run with Docker for easy deployment.
