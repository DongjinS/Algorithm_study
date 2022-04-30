def unique_chk(relation, combi, candidate_key):
    for row in relation:
        keys = []
        for key in combi:
            keys.append(row[key])
        candidate_key[tuple(keys)]+=1
        if candidate_key[tuple(keys)]>1:
            return False
    if len(candidate_key.keys())==len(relation):
        return True

def minimum_chk(candidate, combi):
    if candidate:
        for candi in candidate:
            if set(candi).issubset(set(combi)):
                return False
    return True

def solution(relation):
    from collections import defaultdict
    from itertools import combinations
    answer = 0
    candidate = []
    n = len(relation[0])
    for i in range(1,n+1):
        combis = list(combinations(range(n),i))
        for combi in combis:
            candidate_key = defaultdict(int)
            #최소성
            if not minimum_chk(candidate, combi):
                continue
            #유일성
            if unique_chk(relation, combi, candidate_key):
                candidate.append(combi)
    answer = len(candidate)
    return answer