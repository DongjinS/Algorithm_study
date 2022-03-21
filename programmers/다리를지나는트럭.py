def solution(bridge_length, weight, truck_weights):
    from collections import deque
    answer = 1
    truck_weights.reverse()
    cur_weight = truck_weights[-1]
    on_bridge = deque()
    on_bridge.append([truck_weights.pop(),0])
    while truck_weights or on_bridge:
        if on_bridge:
            for i in range(len(on_bridge)):
                on_bridge[i][1] += 1
            if on_bridge[0][1] >= bridge_length:
                out = on_bridge.popleft()
                cur_weight -= out[0]
                
        if truck_weights and truck_weights[-1] + cur_weight <= weight:
            new_truck = truck_weights.pop()
            on_bridge.append([new_truck, 0])
            cur_weight += new_truck
        
        answer += 1
        
    return answer