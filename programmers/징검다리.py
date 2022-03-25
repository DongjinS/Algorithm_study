def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    distances = []
    for i, location in enumerate(rocks):
        if i == 0:
            distances.append(location-0)
        else:
            distances.append(location-rocks[i-1])
    
    
    for i in range(n): 
        cur_min = min(distances)
        for j in range(len(distances)):
            if distances[j] == cur_min:
                distances[j+1] += cur_min
                del distances[j]
                break
                
    
    answer = min(distances)
    return answer

solution(25, [2, 14, 11, 21, 17], 2)