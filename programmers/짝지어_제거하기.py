def solution(s):
    from collections import deque
    answer = -1
    s = list(s)
    # dq = deque(s)
    container = []
    cnt = 0
    flag = False
    while s:
        n = len(s)
        cnt += 1
        if n>1 and s[-1] == s[-2]:
            s.pop()
            s.pop()
        else:
            container.append(s.pop())
            
        if not s:
            s = container
            if n != len(container):
                flag  = True
            cnt = 0
        
        if cnt == n and flag == False:
            answer = 0
            break
    
    if answer == -1:
        answer = 1
    
    return answer