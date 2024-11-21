
# SoaPractica - Health Check API

Este proyecto es una API diseñada para monitorear la salud de microservicios y RabbitMQ utilizando **FastAPI**. Incluye endpoints para verificar la conectividad y operatividad de los servicios de usuarios, órdenes, notificaciones, y RabbitMQ.

## 🚀 Características

- **Health Check**: Endpoint `/health` que verifica el estado de:
  - RabbitMQ
  - Microservicio de Usuarios
  - Microservicio de Órdenes
  - Microservicio de Notificaciones
- **Arquitectura Modular**: Código organizado en routers y servicios.
- **RabbitMQ Health Check**: Verifica la conectividad con RabbitMQ.
- Implementado con **FastAPI** para rapidez y escalabilidad.

---

## 📂 Estructura del Proyecto

```plaintext
SoaPractica/
├── requirements.txt          # Dependencias del proyecto
├── app/
│   ├── main.py               # Archivo principal de la API
│   ├── config.py             # Configuración de URLs y RabbitMQ
│   ├── routers/              # Routers para servicios y health check
│   │   ├── health_check.py
│   │   ├── users_service.py
│   │   ├── orders_service.py
│   │   └── notification_service.py
│   ├── services/             # Servicios reutilizables
│   │   ├── health_check_service.py
│   │   └── rabbitmq.py
```

---

## ⚙️ Requisitos

- Python 3.8 o superior
- RabbitMQ instalado y ejecutándose
  - Puedes usar Docker:
    ```bash
    docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
    ```
    Acceso a la interfaz de administración: [http://localhost:15672](http://localhost:15672)
    - Usuario: `guest`
    - Contraseña: `guest`

---

## 🛠️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/SoaPractica.git
   cd SoaPractica
   ```

2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate      # Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Ejecución

### 1. Iniciar los Microservicios

Ejecuta los siguientes comandos en diferentes terminales para iniciar los microservicios:

- **Users Service**:
  ```bash
  uvicorn app.routers.users_service:router --port 8000
  ```

- **Orders Service**:
  ```bash
  uvicorn app.routers.orders_service:router --port 8001
  ```

- **Notification Service**:
  ```bash
  uvicorn app.routers.notification_service:router --port 8002
  ```

### 2. Iniciar la API Principal

En otra terminal, ejecuta la API principal:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

---

## 🧪 Pruebas

### Endpoint `/health`
Este endpoint verifica la salud de todos los servicios (RabbitMQ, usuarios, órdenes y notificaciones).

Prueba el endpoint con **curl**:
```bash
curl http://localhost:8080/health
```

Respuesta esperada:
```json
{
    "status": "ok",
    "services": {
        "rabbitmq": {
            "status": "healthy",
            "details": "RabbitMQ is operational"
        },
        "users_service": {
            "status": "healthy",
            "details": {
                "status": "healthy",
                "service": "Users Service"
            }
        },
        "orders_service": {
            "status": "healthy",
            "details": {
                "status": "healthy",
                "service": "Orders Service"
            }
        },
        "notifications_service": {
            "status": "healthy",
            "details": {
                "status": "healthy",
                "service": "Notification Service"
            }
        }
    }
}
```

---

## 🌐 Configuración

Edita el archivo `app/config.py` para personalizar las URLs de los servicios o cambiar la configuración de RabbitMQ.

```python
RABBITMQ_URL = "amqp://guest:guest@localhost:5672/"
USERS_SERVICE_URL = "http://localhost:8000/health"
ORDERS_SERVICE_URL = "http://localhost:8001/health"
NOTIFICATIONS_SERVICE_URL = "http://localhost:8002/health"
```

---

## 🛠️ Solución de Problemas

1. **RabbitMQ no responde**:
   - Asegúrate de que RabbitMQ esté corriendo:
     ```bash
     docker start rabbitmq
     ```
   - Verifica su estado accediendo a: [http://localhost:15672](http://localhost:15672).

2. **Un microservicio no responde**:
   - Asegúrate de que el microservicio correspondiente esté ejecutándose en el puerto correcto.

3. **Error de dependencias**:
   - Asegúrate de instalar las dependencias correctamente:
     ```bash
     pip install -r requirements.txt
     ```

---

## 📖 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para mejoras.

---

## 🧑‍💻 Autor

**Jesús David Ruiz García**  
Si tienes preguntas o comentarios, no dudes en contactarme.
