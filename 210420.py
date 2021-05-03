def solution(name):
    answer = 0
    
    l={"A":0, "B":1, "C":2, "D":3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'Z':1, 'Y':2, 'X':3, 'W':4, 'V':5, 'U':6, 'T':7, 'S':8, 'R':9, 'Q':10, 'P':11, 'O':12, 'N':13}
    for i in range(0, len(name)) :
        letter = name[i]
        answer += l.get(letter)
        if name[0]==A :
            
        if i<len(name)-1 :
            if name[i]!=name[i+1] :
                if name[i+1]!='A' :
                    answer+=1

    return answer
a = solution('ABAA')
b = solution('ANN')
print(a)
print(b)


'''
A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8, J=9, K=10, L=11, M=12
Z=1, Y=2, X=3, W=4, V=5, U=6, T=7, S=8, R=9, Q=10, P=11, O=12, N=13
'''
