from collections import defaultdict
from itertools import combinations
def solution(orders, course):
    candidate = [[] for i in range(len(course))]
    answer = set()
    order_combi_cnt = defaultdict(int) 

    for order in orders:
        for i in range(2,len(order)+1):
            for combi in combinations(order,i):
                combi = list(combi)
                combi.sort()
                order_combi_cnt[tuple(combi)]+=1

    for combi in order_combi_cnt:
        for i in range(len(course)):
            if len(combi)==course[i] and order_combi_cnt[combi] >= 2:
                candidate[i].append([order_combi_cnt[combi],list(combi)])
        
    for can in candidate:
        if can:
            tmp_max, menu = max(can)
            answer.add("".join(menu))
            for cur_cnt, menu in can:
                if tmp_max == cur_cnt:
                    answer.add("".join(menu))
    
    answer = list(answer)
    answer.sort()
    return answer

solution(["XYZ", "XWY", "WXA"], [2, 3, 4])

# 정확성  테스트
# 테스트 1 〉	통과 (0.32ms, 10.3MB)
# 테스트 2 〉	통과 (0.18ms, 10.2MB)
# 테스트 3 〉	통과 (0.17ms, 10.3MB)
# 테스트 4 〉	통과 (0.18ms, 10.2MB)
# 테스트 5 〉	통과 (0.15ms, 10.2MB)
# 테스트 6 〉	통과 (0.39ms, 10.3MB)
# 테스트 7 〉	통과 (0.42ms, 10.3MB)
# 테스트 8 〉	통과 (6.24ms, 10.6MB)
# 테스트 9 〉	통과 (5.99ms, 10.5MB)
# 테스트 10 〉	통과 (8.11ms, 10.9MB)
# 테스트 11 〉	통과 (4.44ms, 10.7MB)
# 테스트 12 〉	통과 (4.22ms, 10.6MB)
# 테스트 13 〉	통과 (8.23ms, 11MB)
# 테스트 14 〉	통과 (9.30ms, 10.8MB)
# 테스트 15 〉	통과 (8.77ms, 10.8MB)
# 테스트 16 〉	통과 (11.57ms, 10.7MB)
# 테스트 17 〉	통과 (18.78ms, 11MB)
# 테스트 18 〉	통과 (21.24ms, 11.2MB)
# 테스트 19 〉	통과 (14.10ms, 10.6MB)
# 테스트 20 〉	통과 (10.87ms, 10.6MB)