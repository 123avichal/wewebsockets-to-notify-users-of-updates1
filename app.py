from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def on_connect():
    socketio.join_room(user_id)

@socketio.on('message')
def on_message(message):
    socketio.emit('notification', message, room=user_id)



if __name__=='__main__':
    socketio.run(app,allow_unsafe_werkzeug=True)