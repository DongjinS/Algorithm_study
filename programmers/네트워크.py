def solution(n, computers):
    from collections import defaultdict
    answer = 0
    
    network = defaultdict(list)
    for i, computer in enumerate(computers):
        for j, connected in enumerate(computer):
            if i != j and connected == 1:
                network[i].append(j)
    
    print(network)
    for computer in range(n):
        stack = []
        if network[computer] and network[computer][-1] != -1:
            stack.append(computer)
            while stack:
                print("stack", stack)
                cur = stack.pop()
                for connected in network[cur]:
                    if network[connected][-1] != -1:
                        if connected not in stack:
                            stack.append(connected)
                network[cur].append(-1)

            answer+=1
        elif network[computer] == []:
            answer+=1
    
    print(answer)
    return answer

solution(3,[[1, 1, 1], [1, 1, 1], [1, 1, 1]])