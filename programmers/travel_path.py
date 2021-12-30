def solution(tickets):
    from collections import defaultdict,deque
    
    connected = defaultdict(deque) #출발 = 키, 도착 = 값 
    path = [] #가능한 경로 저장

    for dep, arr in tickets:
        connected[dep].append(arr)

    def dfs(dep,tmp_path,connected):
        if len(tmp_path) == len(tickets)+1:
            if path:
                if path[-1][1][0]>=tmp_path[1][0]: #이전에 들어온 경로의 첫 도착지의 첫글자보다 같거나 작은 것만 추가
                    path.append([x for x in tmp_path])        
            else:
                path.append([x for x in tmp_path]) # 기존 경로 존재 하지 않으면 추가 x
            return
        for i in range(len(connected[dep])):
            arr = connected[dep].popleft()
            tmp_path.append(arr)
            dfs(arr,tmp_path,connected)
            connected[dep].append(arr)
            tmp_path.pop()
        return

    #BFS? DFS? 인천 출발 도착지 부터 탐색 시작
    for i in range(len(connected['ICN'])):
        first_arr = connected['ICN'].popleft() #방문할 곳이므로 빼준다
        tmp_path = ['ICN']
        tmp_path.append(first_arr) #경로 추적
        dfs(first_arr,tmp_path,connected)
        tmp_path.pop()
        connected['ICN'].append(first_arr) #다른 경로로 타고 들어왔을때 갈 수 있는 곳으로 되어 있어야 하기 때문에 다시 추가
    
    # 찾은 경로가 하나면 바로 리턴
    if len(path) == 1:
        return path[0]
    else:
        tmp_min = path[0] #아니라면 찾은 경로 중 사전 순으로 가장 빠른 것 찾기
        for i in range(1,len(path)):
            for tmp, p in zip(tmp_min, path[i]):
                flag = 0
                for j in range(3):
                    if tmp[j]>p[j]:
                        tmp_min = path[i]
                        flag = 1
                        break
                    elif tmp[j]<p[j]:
                        flag = 1
                        break
                if flag == 1:
                    break
    answer = tmp_min
    return answer

#테케

# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
# solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]])
# solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]])
# solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]])

# 답
# ["ICN", "JFK", "HND", "IAD"]
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
#["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"]
# ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
#  ["ICN", "B", "ICN", "A"]

# 테스트 1 〉	통과 (178.20ms, 15.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)