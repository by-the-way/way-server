# uber_server

������Ϣ��Ĭ�ϸ�ʽ��

    {
        status: 0:��ȷ����0:������,
        message:"xxxxx"
        data:"{
            uid:"xxx"
            icon_url:"xxx"
            .....
            .....
        }"
    }

�ӿ�1���û��״�����app�Զ�ע��Ϊ�û�

    ����ʱ�����û��״�����appʱ

    �������ݣ�{"uid":"xxxxxx"}

    �������ݣ�{"status":0,"message":"xxxx"} 0:succeed, !=0: ʧ��
    
    demo: 192.168.10.115:8001/user_register?json={"uid":"xxxxxx"}

�ӿ�2�������û�����

    ����ʱ�����״�����ʱѡ����˱�ǩ������ͨ������ҳ���޸ĸ�������

    �������ݣ�{"uid":"[userid]","gender":"�У�1��Ů��0","tag":"[������Ư��]","icon_url":"binary","uber_id":"xxx","uber_secret":"xxxx","password":"xxxx"}, uid�Ǳ���ģ�������ѡ

    �������ݣ�Ĭ�ϸ�ʽ

    demo: 192.168.10.115:8001/user_profile?json={"uid":"[userid]","gender":"�У�1��Ů��0","tag":"[������Ư��]","icon_url":"binary","icon_url":"xxx","uber_id":"xxx","uber_secret":"xxxx","password":"xxxx"}

�ӿ�3������(��ȡ)��ǩ

    ����ʱ�����û�������uberȥĳ������λ��
    
    (��ȡ�ӿڣ�{"uid":"xxx"}, 192.168.10.115:8001/event_label?json={"uid":"[userid]"})
    
    ��������,data�����ݣ�{"label_id":"һ��Է�","label_id":"������",....} 
    
    demo: 192.168.10.115:8001/event_label?json={"uid":"[userid]"
    
�ӿ�4���û���ĳ����ǩ����Ȥ

    ����ʱ�����û������һ����Ȥ��ǩ
    
    �������ݣ�{"uid":"xxx","label_id":"xxx"}
    
    �������ݣ�Ĭ�ϸ�ʽ 
    
    demo: 192.168.10.115:8001/selected_label?json={"uid":"[userid]","label":"xxx"})


�ӿ�5����ѯ��ĳ����ǩ����Ȥ�������û�

    ����ʱ�����û������һ����Ȥ��ǩ���Ժ�
    
    �������ݣ�{"uid":"xxx"}
    
    �������ݣ�{"users":[{"uid":"xxx","icon_url":"xxx","tag":"xxx","gender":"xxx"},{"uid":"xxx","icon_url":"xxx","tag":"xxx","gender":"xxx"}]} 
    
    demo: 192.168.10.115:8001/same_user?json={"users":[{"uid":"xxx","icon_url":"xxx","tag":"xxx","gender":"xxx"},{"uid":"xxx","icon_url":"xxx","tag":"xxx","gender":"xxx"}]}

    
    
    
    