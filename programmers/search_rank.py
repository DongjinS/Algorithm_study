def solution(info, query):
    from collections import defaultdict
    from itertools import combinations
    from bisect import bisect_left
    answer = []
    db = defaultdict(list)    
    for one_info in info:
        lang, end, work_ex, food, score = one_info.split(" ")

        for n in range(5):
            combi = list(combinations(range(4),n))
            for c in combi:
                t_c = [lang, end, work_ex, food]
                for v in c:
                    t_c[v] = "-"
                changed_t_c = "/".join(t_c)
                db[changed_t_c].append(int(score))
    
    for value in db.values():
        value.sort()
    
    
    for q in query:
        q = q.split()
        q = [i for i in q if i != "and"]
        score = int(q[-1:][0])
        q = q[:-1]
        cnt = 0
        i = bisect_left(db["/".join(q)],score)
        
        if i<len(db["/".join(q)]):
            cnt = len(db["/".join(q)])-i
        
        answer.append(cnt)
    
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])