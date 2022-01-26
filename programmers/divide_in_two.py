from collections import defaultdict
def traverse(start, graph, visited, n, cnt):
    if len(visited) == n:
        return cnt
    for end in graph[start]:
        if end not in visited:
            visited.add(end)
            cnt = traverse(end, graph, visited, n, cnt+1)
    
    return cnt

def solution(n, wires):
    answer = float('inf')
    for i in range(n-1):
        divided = wires[:i]+wires[i+1:]
        graph = defaultdict(list)
        visited = set()
        cmp_tmp = []
        tmp_ans = 0
        for start, end in divided:
            graph[start].append(end)
            graph[end].append(start)
        # print(graph)
        
        if start not in visited:
            visited.add(start)
            cnt = 1
            cmp_tmp = (traverse(start, graph, visited, n, cnt))        
        
        tmp_ans = abs(cmp_tmp - (n - cmp_tmp))
        
        answer = min(answer, tmp_ans)

    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]),3)
print(solution(4, [[1,2],[2,3],[3,4]]),0)
print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]),1)
