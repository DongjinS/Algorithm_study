def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    
    while progresses:
        for i in range(len(progresses)):
            if progresses[i]<100:
                progresses[i]+=speeds[i]
        
        count = 0
        while progresses and progresses[-1]>=100:
            progresses.pop()
            count+=1
        if count:
            answer.append(count)
    
    return answer