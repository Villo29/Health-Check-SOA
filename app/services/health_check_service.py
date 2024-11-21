import requests

def check_service_health(url: str) -> dict:
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return {"status": "healthy", "details": response.json()}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
    return {"status": "unhealthy", "details": "Service not responding"}
