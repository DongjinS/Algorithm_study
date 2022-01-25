def solution(land):
    for i in range(1,len(land)):
        for j in range(4):
            cur = land[i][j]
            for z in range(4):
                if j!=z:
                    land[i][j] = max(land[i][j],cur+land[i-1][z])
                    
    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]),16)