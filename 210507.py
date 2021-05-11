def solution(citations):
    
    citations.sort()
    ## print("sorted: ",citations)
    l = len(citations)//2
    target = citations[l]
    remain = len(citations)-l-1
    while True :
        
        if target == remain :
            return target
        elif target > remain :
            l-=1
            target = citations[l]
            if l == 0 :
                if citations[0] > remain :
                    return len(citations)
                
            if remain < len(citations)-1 :
                remain+=1
                if remain > target :
                    return remain
        elif target < remain :
            l+=1
            target = citations[l]
            remain-=1
            if target > remain :
                return citations[l-1]
    
    

##a = solution([10,50,100])
##print(a)