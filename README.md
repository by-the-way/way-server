# uber_server

接口1：用户首次启动app自动注册为用户

    请求时机：用户首次启动app时

    发送数据：{"register":ios-device-id,"uid":"xxxxxx"}

    返回数据：{"ret":"ok/error"} 失败或者超时后重新发送

demo: 192.168.10.251:8001/user?json={"register":ios-device-id,"uid":"xxxxxx"}

接口2：设置用户资料

    请求时机：首次启动是选择个人标签，或者通过设置页面修改个人资料

    发送数据：{"id":"[userid]","gender":"女","tag":"[技术，漂亮]","icon":"binary","icon":"xxx","uber_id":"xxx","uber_key":"xxxx","password":"xxxx"}, id是必须的，其它可选

    返回数据：{"ret":"ok/error"} 失败或者超时后重新发送

demo: 192.168.10.251:8001/user?json={"event":"profile"，"id":"[userid]","gender":"女","tag":"[技术，漂亮]","icon":"binary","icon":"xxx","uber_id":"xxx","uber_key":"xxxx","password":"xxxx"}
