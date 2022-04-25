def solution(N, stages):
    from collections import defaultdict
    answer = []
    pn = len(stages)
    rates = []
    for i in range(N):
        n = stages.count(i+1)
        if pn != 0:
            rate = n/(pn)
        else:
            rate = 0
        rates.append((rate,i+1))
        pn-=n
    
    # print(rates)
    answer = list(map(lambda x:x[1], sorted(rates, key=lambda x:x[0], reverse=True)))
    
##tc22 시간초과 버전
#     stage_rate = [[0 for x in range(3)] for x in range(N+1)]
    
#     for i,rate in enumerate(stage_rate):
#         rate[2] = i+1
    
#     for p in stages:
#         stage_rate[p-1][0] += 1
#         stage_rate[p-1][1] += 1
#         for s in range(1,p):
#             stage_rate[s-1][1] += 1 

#     stage_rate.pop()
#     for rate in stage_rate:
#         if rate[1]:
#             rate.append(rate[0]/rate[1])
#         else:
#             rate.append(0)
    
#     stage_rate = sorted(stage_rate,key=lambda x:x[3], reverse=True)
#     answer = list(map(lambda x:x[2], stage_rate))

    return answer