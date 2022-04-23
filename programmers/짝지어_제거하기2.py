def solution(s):
    answer = -1
    
    s = list(s)
    stack = []
    stack.append(s[0])
    
    n = len(stack)
    for i in range(1,len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] != s[i]:
                stack.append(s[i])
            else:
                stack.pop()
    
    if stack:
        answer = 0
    else:
        answer = 1
    
    return answer