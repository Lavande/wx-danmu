# wx-danmu

将微信公众号后台接收的消息实时变成弹幕显示在网页上。

介绍
------

后端基于flask，和前端用socketio通信，前端直接用了[别人的代码](https://github.com/jamesliu96/Damoo/)

依赖：flask、flask-socketio、xmltodict

配置
------

首次需要设置微信公众号后台绑定服务器，在wxverify.py填上你的token然后用flask运行，验证服务器即可绑定。
然后在danmu.py填上服务器地址和token。

运行
------
一个直接但不推荐的方法
```
export FLASK_APP=danmu.py
flask run --host=0.0.0.0 --port=80
```
推荐使用gunicorn并使用nginx反代（其实我自己没搞定所以不举例说明了）
使用
------

用浏览器访问： 你的服务器url + /danmu  这个页面即可，然后尝试用手机往公众号后台发消息。
