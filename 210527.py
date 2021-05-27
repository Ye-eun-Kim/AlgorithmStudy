def solution(n,a,b):
    answer = 0
    while a!=b:
        a= (a+1)//2
        b= (b+1)//2
        answer+=1
    return answer

# 코드 참고: https://jjingho.tistory.com/27
'''
* 이 코드 이해 안 됨
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
'''