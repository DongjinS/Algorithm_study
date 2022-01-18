from collections import deque, defaultdict
import heapq
def dijkstra(start, des, n, graph):
    table = defaultdict(int)
    for i in range(1,n+1):
        table[i] = float("inf")
    
    table[start] = 0
    q = [[0,start]]
    while q:
        accum_cost, start = heapq.heappop(q)
        if table[start]>=accum_cost:
            for fare, end in graph[start]:
                if table[end] > accum_cost+fare:
                    table[end] = accum_cost+fare
                    heapq.heappush(q,[accum_cost+fare, end])
                
    return table[des]

def solution(n, s, a, b, fares):
    graph = defaultdict(list)

    for start, end, fare in fares:
        graph[start].append([fare,end])
        graph[end].append([fare,start])

    cost = dijkstra(s,a,n, graph)+dijkstra(s,b,n, graph)

    for i in range(1, n+1):
        if s != i:
            cost = min(cost, dijkstra(s,i,n, graph)+dijkstra(i,a,n, graph)+dijkstra(i,b,n, graph)) # i까지 합승후 갈리질때 최소금액 최신화

    return cost


solution(6,	4,	5,	6,	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])