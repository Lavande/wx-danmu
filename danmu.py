from flask import Flask, request, render_template
from flask_socketio import SocketIO


# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = 'eventlet'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



@app.route('/danmu')
def index():
    return render_template('danmu.html', async_mode=socketio.async_mode)

@app.route('/trigger')
def trigger():
    danmu = request.args.get('danmu', '')
    print(danmu)
    socketio.emit('my_response',
        {'data': danmu},
        namespace='/channel')
    return 'emitted!'
    

if __name__ == '__main__':
    socketio.run(app)
    #app.run(debug=True, port=5005, host='127.0.0.1')