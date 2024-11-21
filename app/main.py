from fastapi import FastAPI
from app.routers import health_check, users_service, orders_service, notification_service

app = FastAPI(
    title="Health Check API",
    description="API for monitoring the health of microservices",
    version="1.0.0"
)

# Agregar rutas
app.include_router(health_check.router)
app.include_router(users_service.router, prefix="/users", tags=["Users Service"])
app.include_router(orders_service.router, prefix="/orders", tags=["Orders Service"])
app.include_router(notification_service.router, prefix="/notifications", tags=["Notification Service"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Health Check API"}
