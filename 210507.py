def solution(citations):
    
    citations.sort()
    print("sorted: ",citations)
    l = len(citations)//2
    target = citations[l]
    remain = len(citations)-l-1
    while True :
        if l == 0 :
            return 0
        if target == remain :
            return target
        elif target > remain :
            l-=1
            target = citations[l]
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
    
    

a = solution([1,5,5,5,5])
print(a)