# 유니온 파인드
def find(x,connected):
    if connected[x] == x:
        return x 
    connected[x] = find(connected[x], connected) 
    return connected[x]

def union(x, y, connected): 
    x = find(x, connected) #x와 y의 루트노드를 찾아준다. 
    y = find(y, connected)
    if x == y: #루드가 같다면 합칠 필요가 없으니 종료 
        return
    connected[x] = y #x의 부모를 y로 만들어 합쳐주기


def solution(n, costs):
    from collections import defaultdict
    connected = defaultdict(int)
    for x in range(n):
        connected[x] = x
    
    costs.sort(key = lambda x:x[2])
    cnt = 0
    for dep,arr,cost in costs:
        if find(dep, connected) != find(arr, connected):
            union(arr, dep, connected)
            cnt += cost

    answer = cnt
    return answer




print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]),4)
print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]), 15)
print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]), 8)
print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]]), 9)
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]), 104)
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]), 11)
print(solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]), 6)
print(solution(5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]), 8)
print(solution(5, [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]]), 8)