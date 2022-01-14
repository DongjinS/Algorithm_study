def solution(routes):
    answer = 1
    routes.sort()
    # print(routes)
    i = 1
    last_camera = routes[0][1]

    while  i < len(routes):
        if last_camera>=routes[i][0]:
            last_camera = min(routes[i][1], last_camera) # 두개 경로 사이에 카메라 놓을 수 있으면 더 먼저 끝나는 곳에 카메라 놓는다
            i+=1
        else:
            answer+=1
            last_camera = routes[i][1]
            i+=1
            
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]),2)
print(solution([[-20,-15], [-14,-13], [-12,-11], [-10,-9]]),4)
print(solution([[-20,-14], [-14,-13], [-13,-11], [-11,-9]]),2)
print(solution([[-20,-9], [-14,-9], [-13,-11], [-11,-9]]),1)
print(solution([[-2,-1], [1,2],[-3,0]]),2) #2
print(solution([[0,0],]),1) #1
print(solution([[0,1], [0,1], [1,2]]),1) #1
print(solution([[0,1], [2,3], [4,5], [6,7]]),4) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]),2) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]),2) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]]),2) #2

# 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.2MB)
# 테스트 4 〉	통과 (0.07ms, 10.2MB)
# 테스트 5 〉	통과 (0.05ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (3.14ms, 10.4MB)
# 테스트 2 〉	통과 (0.89ms, 10.4MB)
# 테스트 3 〉	통과 (2.53ms, 10.5MB)
# 테스트 4 〉	통과 (0.14ms, 10.2MB)
# 테스트 5 〉	통과 (2.96ms, 10.7MB)