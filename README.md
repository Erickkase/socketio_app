# Flask-SocketIO App

Este proyecto usa Flask y Socket.IO para comunicación en tiempo real.

## 🚀 Ejecutar desde imagen pública (después de subir a Docker Hub)

```bash
docker pull TU_USUARIO/socketio_app
docker run -p 5000:5000 TU_USUARIO/socketio_app
```

## 🛠 Ejecutar localmente (build propio)

```bash
git clone https://github.com/TU_USUARIO/socketio_app.git
cd socketio_app
docker build -t socketio_app .
docker run -p 5000:5000 socketio_app
```

## 📂 Contenido

- `main.py`: servidor Flask con SocketIO
- `templates/templates.html`: plantilla HTML
- `Dockerfile`: configuración de Docker
- `requirements.txt`: dependencias
