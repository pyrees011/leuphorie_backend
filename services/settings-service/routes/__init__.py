from fastapi import APIRouter
from .services import profile, notifications, preferences, reset

router = APIRouter()

router.include_router(profile.router, prefix="/settings", tags=["Profile"])
router.include_router(notifications.router, prefix="/settings", tags=["Notifications"])
router.include_router(preferences.router, prefix="/settings", tags=["Preferences"])
router.include_router(reset.router, prefix="/settings", tags=["Reset"])