def solution(gems):
    from collections import defaultdict
    answer = []
    
    shopped = defaultdict(int)
    start=0
    end = 0
    N = len(gems)
    dN = len(set(gems))
    candidate = []
    
    while True:
        if start == N:
            break
        elif len(shopped) == dN:
            candidate.append([start, end, end-start])
            shopped[gems[start]] -= 1
            if shopped[gems[start]] == 0:
                del shopped[gems[start]]
            start+=1
        elif len(shopped) != dN:
            if end == N:
                break
            shopped[gems[end]] += 1
            end+=1
            
    if candidate:
        candidate.sort(key=lambda x:x[2])
        answer = [candidate[0][0]+1, candidate[0][1]]
    else:
        answer = [1,N]
    return answer

solution(["AA", "AB", "AC", "AA", "AC"])