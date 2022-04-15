def dfs(cur_score, cur_n, cur_candi, n, candidate, score_dict):
    if cur_n==n:
        print(cur_candi)
        candidate.append(cur_candi)
        return

    for i in range(1, cur_score+1):
        next_score = cur_score-i
        if cur_n+score_dict[next_score]<=n:
            next_n = cur_n + score_dict[next_score]
            # print(next_score, cur_score)
            cur_candi[10-next_score] = score_dict[next_score]
            if cur_candi not in candidate:
                dfs(next_score, next_n, cur_candi, n, candidate, score_dict)
    


def solution(n, info):
    from collections import defaultdict
    answer = []
    apeach_score = info
    score_dict = defaultdict(int)
    cost_dict = defaultdict(list)
    candidate = []

    for i in range(11):
        score_dict[10-i] = info[i]+1
        # cost_dict[info[i]+1].append(10-i)
        
    print(score_dict)

    for i in range(11):
        cur_candi = [0,0,0,0,0,0,0,0,0,0,0]
        cur_candi[i] = score_dict[10-i]
        dfs(10-i,score_dict[10-i],cur_candi, n, candidate, score_dict)
    
    print("candidate")
    print(candidate)
    
    return answer

solution(5,	[2,1,1,1,0,0,0,0,0,0,0])