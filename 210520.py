import re
def solution(str1, str2):
    '''str1 = re.sub('[^A-Za-z]', '', str1)
    str1 = str1.upper()
    str2 = re.sub('[^A-Za-z]', '', str2)
    str2 = str2.upper()'''
    small = {}
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

'''
    def solution(str1, str2):
	list_str1 =[]
	list_str2 =[]

	for s1, slice_s1 in zip(str1, str1[1:]) :   # str1 문자만 2글자씩 뽑기
		join_str = "".join([s1,slice_s1])
		if join_str.isalpha() :
			list_str1.append( join_str.lower() )
	
	for s2, slice_s2 in zip(str2, str2[1:]) :    # str2 문자만 2글자씩 뽑기
		join_str = "".join([s2,slice_s2])
		if join_str.isalpha() :
			list_str2.append(join_str.lower())
			

	if len(list_str1) > len(list_str2) : 
	#교집합의 개수를 구함
		inter =  [list_str1.remove(x) for x in list_str2 if x in list_str1] 
	else :
		inter = [list_str2.remove(x) for x in list_str1 if x in list_str2] 

	#합집합은 교집합 + 나머지 원소들 

	list_uni = list_str1 + list_str2
	uni = len(list_uni)
	
	if uni ==0 :
		return 65536
    
	return int(len(inter)/uni * 65536 )
'''