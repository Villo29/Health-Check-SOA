from fastapi import APIRouter
from app.services.rabbitmq import check_rabbitmq_health
from app.config import USERS_SERVICE_URL, ORDERS_SERVICE_URL, NOTIFICATIONS_SERVICE_URL
from app.services.health_check_service import check_service_health

router = APIRouter()

@router.get("/health", tags=["Health Check"])
async def health_check():
    services_health = {
        "rabbitmq": check_rabbitmq_health(),
        "users_service": check_service_health(USERS_SERVICE_URL),
        "orders_service": check_service_health(ORDERS_SERVICE_URL),
        "notifications_service": check_service_health(NOTIFICATIONS_SERVICE_URL),
    }
    return {"status": "ok", "services": services_health}
