import re
def solution(str1, str2):
    '''str1 = re.sub('[^A-Za-z]', '', str1)
    str1 = str1.upper()
    str2 = re.sub('[^A-Za-z]', '', str2)
    str2 = str2.upper()'''
    small = dict()
    big = []
    _union = 0
    _intersection = 0

    if len(str1) >= len(str2) :
        long = str1
        short = str2
    else :
        long = str2
        short = str1
    long_len = len(long)
    short_len = len(short)
    for i in range(short_len-1):
        _key = short[i]+short[i+1]
        _key = re.sub('[^A-Za-z]', '', _key)
        _key = _key.upper()
        if len(_key) != 2:
            continue
        if _key in small:
            small[_key] +=1 
        else :
            small[_key] = 1
    for j in range(long_len-1):
        factor = long[j]+long[j+1]
        factor = re.sub('[^A-Za-z]', '', factor)
        factor = factor.upper()
        if len(factor) != 2:
            continue
        if factor in small :
            if small[factor] == 0:
                _union = _union+1
            else :
                _intersection+=1
                small[factor]-=1
        else :
            _union+=1
    _union = _union + _intersection + sum(small.values())
    if _union != 0:
        _result = _intersection / _union * 65536
        result = int(_result)
        return result
    else :
        
        return 65536
    

str1 = "E=M*C^2"
str2 = "e=m*c^2"
a = solution(str1, str2)
print(a)