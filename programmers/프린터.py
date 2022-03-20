def solution(priorities, location):
    from collections import deque
    
    answer = 0
    target_priorities = []
    for i in range(len(priorities)):
        if i == location:
            target_priorities.append([1,priorities[i]])
            target = target_priorities[i]
        else:
            target_priorities.append([0,priorities[i]])
    
    target_priorities = deque(target_priorities)
    priorities = deque(priorities)
    cur = []
    cnt = 0
    while target_priorities and cur != target:
        cur = target_priorities.popleft()
        priorities.popleft()
        if priorities and max(priorities) > cur[1]:
            priorities.append(cur[1])
            target_priorities.append(cur)
            cur = []
        else:
            print(cur)
            cnt+=1
    print(cnt)
    return cnt

solution([1, 1, 9, 1, 1, 1],	0)