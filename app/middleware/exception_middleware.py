import logging
import traceback
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import HTTPException

logger = logging.getLogger("uvicorn.error")

class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as exc:
            logger.warning(f"HTTPException: {exc.detail} (status {exc.status_code})")
            return JSONResponse(
                status_code=exc.status_code,
                content={"detail": exc.detail}
            )
        except Exception as exc:
            tb = traceback.format_exc()
            logger.error(f"Unhandled Exception: {exc}\n{tb}")
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"}
            )

# To use: app.add_middleware(ExceptionMiddleware)
