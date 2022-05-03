def dfs(nsheep, nwolf, cur, adjacent, info, graph):
    if info[cur]:
        nwolf+=1
    else:
        nsheep+=1

    if nwolf>=nsheep:
        return 0

    sheep_max = nsheep

    for adj in adjacent:
        for n in graph[adj]:
            if n not in adjacent:
                adjacent.add(n)
                sheep_max = max(sheep_max,dfs(nsheep, nwolf, n, adjacent, info, graph))
                adjacent.remove(n)
    
    return sheep_max

def solution(info, edges):
    from collections import defaultdict
    answer = 0
    
    graph = defaultdict(list)
    for s,e in edges:
        graph[s].append(e)
        graph[e].append(s)

    print(graph)
    adjacent = set()
    adjacent.add(0)
    answer = dfs(0, 0, 0, adjacent, info, graph)
    
    print(answer)
    return answer

solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])

