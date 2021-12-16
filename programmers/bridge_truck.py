def solution(bridge_length, weight, truck_weights):
    from collections import deque
    wait_list = deque(truck_weights)
    in_bridge = deque()
    i = 0
    while wait_list or in_bridge:
        i+=1
        #다리에서 나갈 수 있는 트럭 먼저 나가줘야 새로운 트럭 들어올 수 있다.
        if in_bridge and (i-in_bridge[0][1])>=bridge_length: # 다리에 올라온 트럭이 있고 다리 끝에 도달했다면 pop
            in_bridge.popleft()
        if wait_list and sum(map(lambda x:x[0], in_bridge)) + wait_list[0] <= weight: # 대기 중인 트럭이 있고 그중 첫번째가 다리에 올라갈 수 있다면 
            cur_truck = wait_list.popleft()
            in_bridge.append((cur_truck,i))
                
    answer = i
    return answer
