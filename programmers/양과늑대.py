# def solution(info, edges):
#     from collections import defaultdict
#     from collections import deque
#     answer = 0
    
#     map = defaultdict(list)
#     for s,e in edges:
#         map[s].append([e,info[e]])
#         map[e].append([s,info[s]])

#     for node in map:
#         map[node].sort(key = lambda x:x[1])

#     print(map)
#     dq = deque([0])
#     nsheep = 0
#     nwolf = 0
#     chk = [True for x in range(len(info))]
#     while dq:
        
#         break
                
#     print(nsheep)
#     return nsheep

def solution(info, edges):
    def nextNodes(v):
        temp = list()
        for e in edges:
            # i는 부모노드, j는 자식노드
            i, j = e
            # 부모노드 번호 비교
            if v == i:
                temp.append(j)
        return temp

    def dfs(sheep, wolf, current, path):
        # 지금 노드 확인, 양 늑대 판별
        if info[current]:
            wolf += 1
        else:
            sheep += 1

        # 늑대가 다 잡아먹음, 무시
        if sheep <= wolf:
            return 0

        # 아니라면 임시 변수에 값 갱신
        maxSheep = sheep

        # 서칭 시작
        for p in path:
            for n in nextNodes(p):
                if n not in path:
                    path.append(n)
                    # 최대 양 판별
                    print(sheep, wolf, n, path)
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n, path))
                    path.pop()
        return maxSheep

    answer = dfs(0, 0, 0, [0])
    print(answer)
    return answer

solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])

