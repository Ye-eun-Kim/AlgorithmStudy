def solution(bridge_length, weight, truck_weights):
    time = 0
    if len(truck_weights) == 1 :
        return bridge_length + 1
    else :
        on = []
        for i in (len(bridge_length)-1) :
            on[i] = 0
        on[len(bridge_length)-1] = truck_weights.pop(0)
        time += 1
        
        for j in (len(truck_weights)) :
            if (sum(bridge_length)+truck_weights[j]) <= weight :
                temp = truck_weights.pop(j)
                bridge_length.append(temp)
                del(bridge_length[0])
                time += 1
                
            else : 
                del(bridge_length[0])
                time += 1
        
            
        
        
    return time