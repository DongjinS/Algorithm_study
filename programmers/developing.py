def solution(progresses, speeds):    
    progresses = list(reversed(progresses))
    speeds = list(reversed(speeds))
    answer = []

    while progresses:
        n = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            n+=1
        if n!=0:
            answer.append(n)

    return answer
