def solution(gems):
    from collections import defaultdict
    answer = []
    
    shopped = defaultdict(int)
    start=0
    end = 0
    N = len(gems)
    dN = len(set(gems))
    Full = False
    candidate = []
    
    while True:
        if not Full and end != N-1:
            shopped[gems[end]] += 1
            end+=1
        else:
            while start != N-1:
                shopped[gems[start]] -= 1
                if len(list(filter(lambda n : n > 0 ,list(shopped.values())))) == dN:
                    start += 1
                    candidate.append([start, end, end-start])
                else:
                    break
            if end == N-1 or start == N-1:
                print("break")
                break
            Full = False
        
        if len(list(filter(lambda n : n > 0 ,list(shopped.values())))) == dN:
            candidate.append([start, end, start+end])
            Full = True
            
    if candidate:
        candidate.sort(key=lambda x:x[2])
        print(candidate)
        answer = [candidate[0][0], candidate[0][1]]
    else:
        answer = [1,N]
    return answer

solution(["AA", "AB", "AC", "AA", "AC"])