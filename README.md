# uber_server

�ӿ�1���û��״�����app�Զ�ע��Ϊ�û�

    ����ʱ�����û��״�����appʱ

    �������ݣ�{"register":ios-device-id,"uid":"xxxxxx"}

    �������ݣ�{"ret":"ok/error"} ʧ�ܻ��߳�ʱ�����·���

demo: 192.168.10.251:8001/user?json={"register":ios-device-id,"uid":"xxxxxx"}

�ӿ�2�������û�����

    ����ʱ�����״�������ѡ����˱�ǩ������ͨ������ҳ���޸ĸ�������

    �������ݣ�{"id":"[userid]","gender":"Ů","tag":"[������Ư��]","icon":"binary","icon":"xxx","uber_id":"xxx","uber_key":"xxxx","password":"xxxx"}, id�Ǳ���ģ�������ѡ

    �������ݣ�{"ret":"ok/error"} ʧ�ܻ��߳�ʱ�����·���

demo: 192.168.10.251:8001/user?json={"event":"profile"��"id":"[userid]","gender":"Ů","tag":"[������Ư��]","icon":"binary","icon":"xxx","uber_id":"xxx","uber_key":"xxxx","password":"xxxx"}
