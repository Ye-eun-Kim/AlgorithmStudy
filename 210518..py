import re
def solution(s):
    result = []
    findall_s = re.findall('\d+', s)

    _set = list(set(findall_s))
    len_set = len(_set)
    
    d = {}

    for i in range(len_set):
        cnt = findall_s.count(_set[i])
        d[i] = cnt
    
    sorted_d = sorted(d.items(), reverse = True, key = lambda x : x[1])

    for j in range(len_set):
        key = sorted_d[j][0]
        changed_to_int = int(_set[key])
        result.append(changed_to_int)

    return result

    '''
    re_s = re.sub("\{|\}","", s)
    splited_s = re_s.split(',')
    '''