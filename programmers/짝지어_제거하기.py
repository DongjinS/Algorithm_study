def solution(s):
    answer = -1
    s = list(s)
    container = []
    cnt = 0
    n = len(s)
    while s:
        cnt += 1
        if len(s)>1 and s[-1] == s[-2]:
            s.pop()
            s.pop()
        else:
            container.append(s.pop())
            if len(container)>1 and container[-1] == container[-2]:
                container.pop()
                container.pop()
            
        if not s:
            if n == len(container):
                answer = 0
                break
            else:
                s = list(container)
                container = []
                n = len(s)
                cnt = 0
    
    if answer == -1:
        answer = 1
    
    return answer

solution("baabaa")