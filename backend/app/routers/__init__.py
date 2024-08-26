from app.routers.auth import router as auth_router
from app.routers.employee import router as employee_router
from app.routers.user import router as user_router


__all__ = ["auth_router", "employee_router", "user_router"]
