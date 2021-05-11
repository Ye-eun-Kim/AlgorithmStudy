def solution(s): 
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)
        elif stack[-1] == i: stack.pop()
        else: stack.append(i)
    if len(stack) == 0: return 1
    else: return 0 


# def solution(string):
#     answer = 0
#     l = len(string)
#     s =[]
#     for j in range(l) :
#         s.append(string[j])
#     for i in range(l-1,1,-1):
#         if s[i-1] == s[i] :
#             print(s[i])
#             # s.pop(s[i-1])
#             # s.pop(s[i-1])
#     return answer


# print(solution("baabaa"))