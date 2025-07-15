import logging
import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger("uvicorn.access")

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response: Response = await call_next(request)
        process_time = (time.time() - start_time) * 1000  # ms
        logger.info(
            f"{request.method} {request.url.path} - Status: {response.status_code} - Time: {process_time:.2f}ms"
        )
        return response

# To use: app.add_middleware(LoggingMiddleware)
