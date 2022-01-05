def solution(triangle):
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
    
    return triangle[0][0]

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.16ms, 10.2MB)
# 테스트 5 〉	통과 (0.98ms, 10.3MB)
# 테스트 6 〉	통과 (0.28ms, 10.3MB)
# 테스트 7 〉	통과 (0.99ms, 10.4MB)
# 테스트 8 〉	통과 (0.21ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.23ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (33.19ms, 14.2MB)
# 테스트 2 〉	통과 (25.67ms, 13.2MB)
# 테스트 3 〉	통과 (34.67ms, 14.7MB)
# 테스트 4 〉	통과 (30.68ms, 14.3MB)
# 테스트 5 〉	통과 (31.09ms, 14MB)
# 테스트 6 〉	통과 (38.54ms, 14.6MB)
# 테스트 7 〉	통과 (36.12ms, 14.4MB)
# 테스트 8 〉	통과 (26.61ms, 13.7MB)
# 테스트 9 〉	통과 (31.21ms, 13.9MB)
# 테스트 10 〉	통과 (33.22ms, 14.5MB)