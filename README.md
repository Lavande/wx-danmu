# wx-danmu

将微信群内接收的消息实时变成弹幕显示在网页上。

介绍
------

后端基于flask，和前端用socketio通信，前端直接用了[别人的代码](https://github.com/jamesliu96/Damoo/)。另外启动一个基于itchat的微信客户端接收群消息，然后向flask服务器后端发送GET请求，后端接收后发到前端显示为弹幕。


配置
------

可以在trigger.py里设置需要接收的群的识别符（参见[itchat文档](https://itchat.readthedocs.io/zh/latest/)），或直接移除条件判断逻辑，显示接受到的所有消息。

运行
------
- 先安装依赖，然后运行flask服务：
`python3 danmu.py`
- 然后运行微信客户端触发机关：
`python3 trigger.py`
- 扫码登录微信即可。

使用
------
用浏览器访问： localhost:5000/danmu 这个页面即可，配合电脑投影到大屏幕效果最佳。
