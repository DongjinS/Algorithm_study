def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    h_candidate = []
    for i in range(n):
        h_cnt = 0
        for j in range(n-1-i,n):
            if citations[n-1-i] <= citations[j]:
                h_cnt += 1
        if h_cnt >= citations[n-1-i]:
            return citations[n-1-i]
#             h_candidate.append(citations[n-1-i])
            
#     print(h_candidate)
#     answer = max(h_candidate)
    return answer