import itchat
from itchat.content import TEXT
import requests


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    #Add your own filter or remove this condition if you want to show all messages
    if msg.User.NickName == '草地6月 清·轻 最可爱班级':
        payload = {'danmu': msg.text}
        requests.get('http://127.0.0.1:5000/trigger', params=payload)


itchat.auto_login(hotReload=True)
itchat.run()