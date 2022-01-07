def solution(money):
    answer = 0
    
    n = len(money)
    if n<=3:    # 집이 3개 이하면 바로 최대값 리턴
        return max(money[0],money[1],money[2])
    
    dp1 = [0 for x in range(n-1)] # 마지막꺼 뺀 dp1   
    dp1[0] = money[0]
    dp1[1] = money[1]

    dp2 = [0 for x in range(n-1)] #첫번째 꺼 뺀 dp2
    dp2[0] = money[1]
    dp2[1] = money[2]

    for i in range(2,len(money)-1):
        dp1[i] = max(money[i]+dp1[i-2], money[i]+dp1[i-3])
    for i in range(2,len(money)-1):
        dp2[i] = max(money[i+1]+dp2[i-2], money[i+1]+dp2[i-3])

    answer = max(dp1[n-2],dp1[n-3],dp2[n-2],dp2[n-3])
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.46ms, 10.3MB)
# 테스트 2 〉	통과 (0.67ms, 10.3MB)
# 테스트 3 〉	통과 (0.36ms, 10.4MB)
# 테스트 4 〉	통과 (0.04ms, 10.3MB)
# 테스트 5 〉	통과 (0.19ms, 10.3MB)
# 테스트 6 〉	통과 (0.41ms, 10.3MB)
# 테스트 7 〉	통과 (0.51ms, 10.3MB)
# 테스트 8 〉	통과 (0.20ms, 10.3MB)
# 테스트 9 〉	통과 (0.70ms, 10.3MB)
# 테스트 10 〉	통과 (0.29ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	통과 (737.45ms, 113MB)
# 테스트 2 〉	통과 (630.19ms, 106MB)
# 테스트 3 〉	통과 (698.61ms, 110MB)
# 테스트 4 〉	통과 (701.31ms, 111MB)
# 테스트 5 〉	통과 (578.06ms, 92.5MB)
# 테스트 6 〉	통과 (675.32ms, 107MB)
# 테스트 7 〉	통과 (402.68ms, 66.5MB)
# 테스트 8 〉	통과 (370.16ms, 68.1MB)
# 테스트 9 〉	통과 (428.55ms, 78MB)
# 테스트 10 〉	통과 (683.16ms, 108MB)

print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)