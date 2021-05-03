def solution(scoville, K):
    import heapq

    cnt = 0

    heapq.heapify(scoville)
    while scoville[0]<K :
        if len(scoville)>1:
            heapq.heappush(scoville, heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
            cnt+=1
        else:
            return -1

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


    ''' 코드 참고: https://yurimkoo.github.io/algorithm/2019/09/26/more-spicy.html
    왜 return -1인지 이유 모름 '''