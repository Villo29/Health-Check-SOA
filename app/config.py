import os

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
USERS_SERVICE_URL = "http://localhost:8000/health"
ORDERS_SERVICE_URL = "http://localhost:8001/health"
NOTIFICATIONS_SERVICE_URL = "http://localhost:8002/health"