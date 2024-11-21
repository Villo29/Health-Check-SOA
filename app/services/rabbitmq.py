import pika
from app.config import RABBITMQ_URL

def check_rabbitmq_health():
    try:
        connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
        connection.close()
        return {"status": "healthy", "details": "RabbitMQ is operational"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
