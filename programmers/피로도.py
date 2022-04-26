def solution(k, dungeons):
    from itertools import permutations
    answer = -1
    # candidate = []
    permu = list(permutations(dungeons,len(dungeons)))
    
    for dungeon in permu:
        tmp = k
        flag = True
        cnt = 0
        for require, needed in dungeon:
            if tmp >= require:
                tmp -= needed
                cnt += 1
            else:
                break
        
        answer = max(cnt,answer)
    
    return answer