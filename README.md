# uber_server

�ӿ�1���û��״�����app�Զ�ע��Ϊ�û�

    ����ʱ�����û��״�����appʱ

    �������ݣ�{"uid":"xxxxxx"}

    �������ݣ�{"status":0,"message":"xxxx"} 0:succeed, !=0: ʧ��
    
    demo: 192.168.10.251:8001/user_register?json={"uid":"xxxxxx"}

�ӿ�2�������û�����

    ����ʱ�����״�������ѡ����˱�ǩ������ͨ������ҳ���޸ĸ�������

    �������ݣ�{"uid":"[userid]","gender":"Ů","tag":"[������Ư��]","icon":"binary","uber_id":"xxx","uber_key":"xxxx","password":"xxxx"}, uid�Ǳ���ģ�������ѡ

    �������ݣ�{"ret":"ok/error"} ʧ�ܻ��߳�ʱ�����·���

    demo: 192.168.10.251:8001/user_profile?json={"uid":"[userid]","gender":"Ů","tag":"[������Ư��]","icon":"binary","icon":"xxx","uber_id":"xxx","uber_key":"xxxx","password":"xxxx"}

�ӿ�3������(��ȡ)��ǩ

    ����ʱ�����û�������uberȥĳ������λ��
    (��ȡ�ӿڣ�{"uid":"xxx"}, 192.168.10.251:8001/event_label?json={"uid":"[userid]"})
    ����/�������ݣ�{label1:"����һ��Է�",label2:"����������"....}
    
    
    
    