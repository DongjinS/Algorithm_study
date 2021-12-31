def solution(n, edge):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    visited = set()
    q = deque()

    for p,c in edge:
        graph[p].append(c)
        graph[c].append(p)
    
    q.append(1)
    
    print(graph)
    visited.add(1)

    while q: 
        answer = len(q)
        for i in range(len(q)):
            v = q.popleft()
            for n in (graph[v]):
                if n not in visited:
                    visited.add(n)
                    q.append(n)
        
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.19ms, 10.3MB)
# 테스트 5 〉	통과 (0.91ms, 10.6MB)
# 테스트 6 〉	통과 (2.47ms, 10.9MB)
# 테스트 7 〉	통과 (19.42ms, 18MB)
# 테스트 8 〉	통과 (41.17ms, 23.2MB)
# 테스트 9 〉	통과 (33.04ms, 23.1MB)
