import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server')
    sio.emit('message', 'Hello from client!')

@sio.on('message')
def on_message(data):
    print('Message from server:', data)

sio.connect('http://localhost:3000')
try:
    sio.wait()
except KeyboardInterrupt:
    print("Interrupted by user. Disconnecting...")
    sio.disconnect()