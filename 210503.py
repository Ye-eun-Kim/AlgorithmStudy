def solution(scoville, K):

    cnt = 0
    ##scoville 정렬
    scoville.sort()
    ##스코빌 지수가 K 미만인 요소의 최대 index 구하기 -> n == K 미만인 요소 개수
    start = 0
    end = len(scoville)-1
    while start <= end :
        mid = (start+end)//2
        if scoville[mid] < K :
            start = mid+1
        elif scoville[mid] > K :
            end = mid -1
        elif scoville[mid] == K :
            end=mid
            break
    n = end

    ##n==1
    while n!=0 :
        if n==1 :
            return cnt+1
        else :
            temp = scoville.pop(0)+scoville.pop(0)*2
            cnt+=1
            scoville.append(temp)
            scoville.sort()
            if temp >= K :
                if n==2 :
                    return cnt
                else :
                    n-=2
            elif temp < K :
                if n==2 :
                    return cnt+1
                else :
                    n-=1
    return cnt

scoville = [1, 2, 3, 9, 10, 12]
K = 7
result = solution(scoville, K)
print(result)


'''
    scoville 정렬
    스코빌 지수가 K 미만인 요소의 최대 index(n=index+1) 구함
    만약 n=1이면 return cnt+1
    만약 n=2이면 아래 과정 거치고, K 미만이면 return cnt+=1.
    제일 적은 두 개(scoville[0:2])로 새로운 음식 만들고 cnt+=1, K와 비교
    -> 크면 n-=2, 남은 것들로 반복
    -> 작으면 남은 것들과 정렬, 위 과정 반복.
    
    '''