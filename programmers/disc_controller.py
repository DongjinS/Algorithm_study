def solution(jobs):
    from heapq import heappush, heappop
    answer = 0
    N = len(jobs)
    time = 0
    jobs.sort()
    hq = []
    while jobs and jobs[0][0]<=time:
        cur = jobs.pop(0)
        heappush(hq, [cur[1],cur[0]])
    flag = 0
    #0초에 요청들어올 경우
    while jobs or hq: 
        if hq:
            finished = heappop(hq)
            time += finished[0] 
            answer += time - finished[1]
            flag = 1
        
        while jobs and jobs[0][0]<=time:
            cur = jobs.pop(0)
            heappush(hq, [cur[1],cur[0]])
            flag = 1
        
        if flag == 1:
            flag=0
        else:
            time+=1
    
    return (answer//N)

solution([[0, 10], [4, 10], [5, 11], [15, 2]] ) #15
# solution([[0, 3], [4, 3], [10, 3]] ) #3
# solution([[0, 10], [4, 10], [15, 2], [5, 11]]) #15
# 테스트 1 〉	통과 (0.50ms, 10.4MB)
# 테스트 2 〉	통과 (0.42ms, 10.3MB)
# 테스트 3 〉	통과 (0.37ms, 10.3MB)
# 테스트 4 〉	통과 (0.39ms, 10.3MB)
# 테스트 5 〉	통과 (0.84ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.34ms, 10.3MB)
# 테스트 8 〉	통과 (0.48ms, 10.3MB)
# 테스트 9 〉	통과 (0.11ms, 10.3MB)
# 테스트 10 〉	통과 (0.51ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (0.02ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
