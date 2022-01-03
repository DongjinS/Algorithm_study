def solution(n, results):
    from collections import defaultdict, deque
    #wtl = winner to loser
    #ltw = loser to winner
    wtl = defaultdict(list)
    ltw = defaultdict(list)
    for winner, loser in results:
        wtl[winner].append(loser)
        ltw[loser].append(winner)

    #순위 정할 수 있는 선수 = 자기 자신을 시작으로 이긴 방향 그래프와 진 방향 그래프를 탐색해서 모든 선수를 방문 가능한 선수..
    ranked_cnt = 0
    for player in range(1,n+1):
        visited = set()
        visited.add(player)
        if wtl[player]:
            q = deque([player])
            while q:
                winner = q.popleft()
                for loser in wtl[winner]:
                    if loser not in  visited:
                        q.append(loser)
                        visited.add(loser)
        if ltw[player]:
            q = deque([player])
            while q:
                loser = q.popleft()
                for winner in ltw[loser]:
                    if winner not in visited:
                        q.append(winner)
                        visited.add(winner)
        
        if len(visited) == n:
            ranked_cnt+=1

    answer = 0
    return answer

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])