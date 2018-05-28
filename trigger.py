import itchat
from itchat.content import TEXT
import requests


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    #Add your own filter or remove this condition if you want to show all messages
    if msg.fromUserName == '@@9397baca73713aca94bf99a304a9c4884d42e4be67b061d987be0aeaaeac851b':
        payload = {'danmu': msg.text}
        requests.get('http://127.0.0.1:5000/trigger', params=payload)


itchat.auto_login(hotReload=True)
itchat.run()