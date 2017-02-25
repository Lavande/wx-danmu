# wx-danmu
======
将微信公众号后台接收的消息实时变成弹幕显示在网页上。

后端基于flask，和前端用socketio通信，前端直接用了[别人的代码](https://github.com/jamesliu96/Damoo/)

依赖flask、flask-socketio、xmltodict

运行
------
一个直接但不推荐的方法
```
export FLASK_APP=danmu.py
flask run --host=0.0.0.0 --port=80
```
推荐使用gunicorn并使用nginx反代（其实我自己没搞定所以不举例说明了）
