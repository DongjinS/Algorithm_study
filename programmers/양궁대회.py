from collections import defaultdict
import copy

def dfs(cur_score, cur_n, cur_candi, n, candidate, score_dict, apeach_score, info):
    if cur_n==n:
        tmp_rival = copy.deepcopy(apeach_score)
        total = 0
        for i in range(11):
            if cur_candi[i]:
                if info[i]:
                    tmp_rival-=10-i
                total += (10-i)
        cur_candi.append(tmp_rival-total)
        candidate.append(cur_candi)
        return

    for i in range(1, cur_score+1):
        next_score = cur_score-i
        next_candi = copy.deepcopy(cur_candi)
        if cur_n+score_dict[next_score]<=n:
            next_n = cur_n + score_dict[next_score]
            next_candi[10-next_score] = score_dict[next_score]
            if next_candi not in candidate:
                dfs(next_score, next_n, next_candi, n, candidate, score_dict,apeach_score, info)
        elif next_score == 0:
            next_candi[10-next_score] = n - cur_n
            next_n = n
            if next_candi not in candidate:
                dfs(next_score, next_n, next_candi, n, candidate, score_dict,apeach_score, info) 

def solution(n, info):
    answer = []
    apeach_score = 0
    score_dict = defaultdict(int)
    cost_dict = defaultdict(list)
    candidate = []

    for i in range(11):
        score_dict[10-i] = info[i]+1
        if info[i]:
            apeach_score += 10-i
        
    for i in range(11):
        cur_candi = [0,0,0,0,0,0,0,0,0,0,0]
        if 0 + score_dict[10-i] <= n:
            cur_candi[i] = score_dict[10-i]
            dfs(10-i,score_dict[10-i],cur_candi, n, candidate, score_dict, apeach_score, info)

    candidate.sort(key=lambda x:x[-1])
    real_candis = []
    diff = candidate[0][-1]
    if diff >= 0:
        return [-1]
    for candi in candidate:
        if candi[-1] == diff:
            real_candis.append(candi[:-1])
        else:
            break
    
    real_candis.sort(key=lambda x:(x[-1],x[-2],x[-3],x[-4],x[-5],x[-6],x[-7],x[-8],x[-9],x[-10]))
    answer = real_candis[-1]
    return answer

solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])