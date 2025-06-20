from flask import Flask, render_template  # Importa Flask y la función para renderizar plantillas HTML
from flask_socketio import SocketIO, send  # Importa SocketIO y la función send para emitir mensajes

# Crea la aplicación Flask
app = Flask(__name__)

# Configura una clave secreta (requerida por Flask-SocketIO para manejar sesiones)
app.config['SECRET_KEY'] = 'secret'

# Inicializa SocketIO con la aplicación Flask
socketio = SocketIO(app)

# Ruta principal del sitio web (http://localhost:5000/)
@app.route('/')
def index():
    # Renderiza el archivo index.html ubicado en la carpeta 'templates'
    return render_template('templates.html')

# Evento manejador para recibir mensajes desde el cliente
@socketio.on('message')
def handle_message(msg):
    print("Mensaje recibido:", msg)  # Imprime el mensaje en la consola del servidor
    send(msg, broadcast=True)        # Reenvía el mensaje a todos los clientes conectados

# Punto de entrada principal para ejecutar el servidor
if __name__ == '__main__':
    # Inicia el servidor con depuración activada
    socketio.run(app, debug=True)
