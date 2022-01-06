def solution(m, n, puddles):
    from collections import deque
    map_to_school = [[0 for y in range(m)] for x in range(n)]
    for x, y in puddles:
        map_to_school[y-1][x-1] = -1
    map_to_school[0][0]=1
    q = deque()
    q.append([0,0])
    while q:
        visited = set()
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x,y) not in visited:
                if x+1<n and map_to_school[x+1][y] != -1:
                    map_to_school[x+1][y]+=map_to_school[x][y]
                    q.append([x+1,y])
                if y+1<m and map_to_school[x][y+1] != -1:
                    map_to_school[x][y+1]+=map_to_school[x][y]
                    q.append([x,y+1])
            visited.add((x,y))
        
    return map_to_school[n-1][m-1]%1000000007

solution(4,3,[[2, 2]])

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (0.08ms, 10.3MB)
# 테스트 5 〉	통과 (0.28ms, 10.3MB)
# 테스트 6 〉	통과 (0.11ms, 10.3MB)
# 테스트 7 〉	통과 (0.12ms, 10.3MB)
# 테스트 8 〉	통과 (0.26ms, 10.3MB)
# 테스트 9 〉	통과 (0.11ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (8.15ms, 10.4MB)
# 테스트 2 〉	통과 (3.60ms, 10.3MB)
# 테스트 3 〉	통과 (6.91ms, 10.3MB)
# 테스트 4 〉	통과 (5.41ms, 10.3MB)
# 테스트 5 〉	통과 (5.79ms, 10.3MB)
# 테스트 6 〉	통과 (7.39ms, 10.3MB)
# 테스트 7 〉	통과 (4.04ms, 10.3MB)
# 테스트 8 〉	통과 (6.16ms, 10.3MB)
# 테스트 9 〉	통과 (6.67ms, 10.4MB)
# 테스트 10 〉	통과 (6.44ms, 10.3MB)