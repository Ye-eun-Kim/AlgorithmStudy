
def solution(numbers):
    '''
    문자열 파싱, 조합해보기-1개, 2개, ... , n개(최대 7개)
    소수인지 판별->소수이면 cnt+=1
    '''

    from itertools import permutations
    import math

    cnt=0
    prime = []
    
    num = list(numbers)
    for k in range (1, len(num)+1) :
        number = list(set(map(''.join, permutations(num, k))))
        
        print("number: ", number)
        for i in range(0, len(number)):
            if number[i][0]==0:
                break
            number_test = int(number[i])
            print("number_test",number_test)
            factor = 0
            if number_test not in prime :
                n = int(math.sqrt(number_test))+1
                if n>2:
                    for j in range(2, n):
                        if number_test%j==0 :
                            factor+=1
                    if factor == 0 :
                        print("prime number: ",number_test)
                        prime.append(number_test)
                        cnt+=1
                elif number_test ==2 :
                    prime.append(number_test)
                    cnt+=1
                elif number_test ==3 :
                    prime.append(number_test)
                    cnt+=1
            
            
        
    return cnt

##test = solution("17")
##print(test)
test = solution("3")
print(test)

'''
<깔끔한 코드>
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        ## |: 합집합 연산자, -: 차집합 연산자
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
    '''