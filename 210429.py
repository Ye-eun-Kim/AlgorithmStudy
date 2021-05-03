'''
numbers의 배열을 바꾼 뒤 문자열로 출력
원소 하나는 최대 3자리(0~999) & 1000
원소의 맨 첫 번째 자릿수 비교 - 모두 세 자리 수로 간주(-> 시간 초과 우려됨)

(첫 번째 자리수) 개수 조사 2차원 리스트 - [0][x]: 0개수, [1][y]: 1개수, [2][z]: 2개수 ....
2차원에서 (첫째 자리수)보다 그 뒷자리수가 큰대로 배열됨. 

'''
def solution(numbers):
    num = [][]
    for number in numbers:
        if number == 1000:
            num[1].append(number)
        else:
            k=number%100
            if k!=0:
                while num[k]:
                    num[k].append(number)
            else:
                k=number%10
            
            

    answer = ''
    return answer