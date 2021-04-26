def solution(bridge_length, weight, truck_weights):
    time = 0
    ## 차가 1개일 때
    if len(truck_weights) == 1 :
        return bridge_length + 1
    ## 차가 1개 초과일 때
    else :
        ## on: 다리 위의 차 상태, bridge_length만큼 0으로 초기화
        
        on = []
        for i in range(bridge_length-1) :
            on.append(0)
        ## 첫 번째 차
        on.append(truck_weights.pop(0))
        time += 1
        
        ## 두 번째 차부터, truck_weights 전부 넣기.
        while truck_weights :
            if (sum(on)+truck_weights[0]) <= weight :
                temp = truck_weights.pop(0)
                on.append(temp)
                del(on[0])
                time += 1
                
            else : 
                del(on[0])
                time += 1

        return time+bridge_length