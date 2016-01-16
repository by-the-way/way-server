# uber_server

接口1：用户首次启动app自动注册为用户

      请求时机：用户首次启动app时

      发送数据：{"register":ios-device-id,"uid":"xxxxxx"}

      返回数据：{"ret":"ok/error"} 失败或者超时后重新发送

demo: 192.168.10.251:8001/user?json={"register":ios-device-id,"uid":"xxxxxx"}