def solution(record):
    answer = []
    userdict = {}
    # mes : record의 message 
    # message를 받음과 동시에 유저 아이디 : 닉네임을 저장 
    # Enter, Change가 들어온 경우 dictionary에 저장
    for mes in record:
        message=(mes.split(' '))
        if (message[0] == 'Enter') | (message[0] == 'Change'):
            userdict[message[1]] = message[2]

    # for문을 돌면서, 하나씩 출력 
    for mes in record:
        message=(mes.split(' '))
        if message[0] == 'Enter': 
            # userdict[message[1]] + '님이 들어왔습니다.' 이런식으로 해도 가능 
            answer.append("{}님이 들어왔습니다.".format(userdict[message[1]]))
        elif mes.split(' ')[0] == 'Leave': 
            answer.append("{}님이 나갔습니다.".format(userdict[message[1]]))
        else:
            pass
    return answer


a=solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(a)

'''
    배열 파싱 -> 2차원 배열로 만듦
    멤버 수 조사 set(record[i][1])
    반복문, len(record)-1부터 시작, 유저의 가장 마지막 닉네임record[][2] 탐색, 없으면 넘어감
    <출력>
    record[][1]->이름 변경, record[][0]->문구 결정
    '''


'''def solution(record):
    answer = []
    members = []
    msg = []

    for i in range(len(record)-1):
        fraction = record[i].split(" ")
        msg.append(fraction)
        user_id = fraction[1]
        members.append(user_id)

    ##print(msg)
    members_set = set(members)
    ##print(members_set)
    
    for j in range(len(record)-1, 0, -1):
        if msg[j][0] == "Enter" | msg[j][0] == "Change" :
            for k in range(len(members_set)):
                if msg[j][1] == members_set[k] :
                    name = msg[j][2]
                    mas[j][2]

            
        
    return answer
'''


