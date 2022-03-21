def solution(citations):
    answer = 0
    n = len(citations)
    h_candidate = []
    for i in range(max(citations)):
        h_cnt = 0
        for j in range(len(citations)):
            if i <= citations[j]:
                h_cnt += 1
        if h_cnt >= i:
            h_candidate.append(i)
    
    if h_candidate:
        answer = h_candidate[-1]
    return answer