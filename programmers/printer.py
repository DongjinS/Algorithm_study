def solution(priorities, location):
    from collections import deque
    candidate = deque()
    for i in range(len(priorities)):
        candidate.append((priorities[i],i))\

    p=0
    while candidate:
        flag = 1
        tmp = candidate.popleft()
        for v,i in candidate:
            if v>tmp[0]:
                candidate.append(tmp)
                flag = 0
                break

        if flag == 1:
            p = p 
            if tmp[1] == location:
                break

    answer = p
    return answer

solution([2, 1, 3, 2], 2)