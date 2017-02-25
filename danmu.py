from flask import Flask, request, render_template
from flask_socketio import SocketIO
import hashlib
import xmltodict
import time


##BASIC SETTINGS##
#set the server's url here
urlbase = 'http://'
#set your token here
token = ''

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = 'eventlet'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None


@app.route('/danmu')
def index():
    return render_template('danmu.html', async_mode=socketio.async_mode)

def Isfromwx(request):
	signature = request.args.get('signature', '')
	timestamp = request.args.get('timestamp', '')
	nonce = request.args.get('nonce', '')
	#echostr = request.args.get('echostr', '')
	L = [token, timestamp, nonce]
	L.sort()
	s = L[0] + L[1] + L[2]
	s = s.encode('utf8')
	if hashlib.sha1(s).hexdigest() == signature:
		return True
	else:
		return False

def xml_msg(user, msg, fromuser):
	'''format the raw message into xml'''

	template = '''
<xml>
<ToUserName><![CDATA[{0}]]></ToUserName>
<FromUserName><![CDATA[{3}]]></FromUserName>
<CreateTime>{1}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{2}]]></Content>
</xml>'''
	return template.format(user, int(time.time()), msg, fromuser)

@app.route('/', methods=['POST', 'GET'])
def get_msg():
	if Isfromwx(request):
		if request.method == 'POST':
			d = request.data
			d = str(d, 'utf-8')
			d = xmltodict.parse(d)
			FromUserName = d['xml']['FromUserName']
			MsgType = d['xml']['MsgType']
			me = d['xml']['ToUserName']

			if MsgType == 'text':
				with open('user_msg', 'a') as f: f.write(str(d)+'\n')
				socketio.emit('my_response',
						{'data': d['xml']['Content']},
						namespace='/test')

				#default auto-reply if we received a non-image message
				msg = '弹幕已上墙，请看大屏幕！'
				xml = xml_msg(FromUserName, msg, me)
				return xml

	#show a blank page for website visitors
	if request.method == 'GET':
		return ''
