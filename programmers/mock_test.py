def solution(answers):
    from collections import deque
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    supo1 = deque(supo1)
    supo2 = deque(supo2)
    supo3 = deque(supo3)
    answers = deque(answers)
    
    while answers:
        ans = answers.popleft()
        tmp = []
        tmp.append(supo1.popleft())
        tmp.append(supo2.popleft())
        tmp.append(supo3.popleft())
        for i in range(3):
            if tmp[i] == ans:
                score[i] += 1
            if i == 0:
                supo1.append(tmp[i])
            elif i == 1:
                supo2.append(tmp[i])
            else:
                supo3.append(tmp[i])
    
    top_scorerer = []
    max_score = max(score)
    for i in range(len(score)):
        if score[i] == max_score:
                top_scorerer.append(i+1)
    
    return top_scorerer