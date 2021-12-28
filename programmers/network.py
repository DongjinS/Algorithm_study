def dfs(computer, network,visited):
    for start in network[computer]:
        if start!= computer and start not in visited:
				#방문할 곳이 자기자신이 아니고 방문체크 되어 있지 않으면 방문체크하고 방문
            visited.add(start)
            dfs(start,network,visited)
    return

def solution(n, computers):
    from collections import defaultdict
    network = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j] != 0:
                network[i].append(j)
    
		# defaultdict(<class 'list'>, {0: [0, 1], 1: [0, 1], 2: [2]})
    visited = set() #방문체크
    cnt = 0 # 탐색 새로 시작하면 네트워크 개수 +1
    
    for start in network:
        if start not in visited:
            visited.add(start)
            dfs(start,network,visited)
            cnt+=1

    answer = cnt
    return answer
    
solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.05ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.36ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.1MB)
# 테스트 8 〉	통과 (0.26ms, 10.3MB)
# 테스트 9 〉	통과 (0.15ms, 10.4MB)
# 테스트 10 〉	통과 (0.14ms, 10.2MB)
# 테스트 11 〉	통과 (0.60ms, 10.3MB)
# 테스트 12 〉	통과 (0.46ms, 10.3MB)
# 테스트 13 〉	통과 (0.24ms, 10.4MB)
