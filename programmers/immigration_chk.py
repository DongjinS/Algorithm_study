def solution(n, times):
    answer = 0
    candidiate_ans = []
    longest = 1000000000

    lp = 0
    rp = longest*n
    middle = (lp+rp)//2

    while lp<=rp:
        possible_num = 0
        for time in times:
            possible_num += middle//time
            if possible_num > n:
                break
        
        if possible_num < n:
            lp = middle+1
        elif possible_num >= n:
            rp = middle-1
            candidiate_ans.append(middle)
            
        middle = (lp+rp)//2

    answer = min(candidiate_ans)
    return answer

solution(10,[6, 8, 10])

# 테스트 1 〉	통과 (0.02ms, 10.4MB)
# 테스트 2 〉	통과 (0.09ms, 10.3MB)
# 테스트 3 〉	통과 (3.44ms, 10.3MB)
# 테스트 4 〉	통과 (159.74ms, 14.3MB)
# 테스트 5 〉	통과 (379.04ms, 14.3MB)
# 테스트 6 〉	통과 (173.80ms, 14MB)
# 테스트 7 〉	통과 (416.60ms, 14.2MB)
# 테스트 8 〉	통과 (442.23ms, 14.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.4MB)


# heapq 사용 시
def solution_h(n, times):
    from heapq import heappush
    answer = 0
    candidiate_ans = []
    longest = 1000000000

    lp = 0
    rp = longest*n
    middle = (lp+rp)//2

    while lp<=rp:
        possible_num = 0
        for time in times:
            possible_num += middle//time
            if possible_num > n:
                break
        
        if possible_num < n:
            lp = middle+1
        elif possible_num >= n:
            rp = middle-1
            heappush(candidiate_ans, middle)
            
        middle = (lp+rp)//2

    answer = candidiate_ans[0]
    return answer

solution_h(10,[6, 8, 10])

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.09ms, 10.2MB)
# 테스트 3 〉	통과 (3.53ms, 10.3MB)
# 테스트 4 〉	통과 (160.23ms, 14.3MB)
# 테스트 5 〉	통과 (346.10ms, 14.3MB)
# 테스트 6 〉	통과 (185.23ms, 14MB)
# 테스트 7 〉	통과 (407.00ms, 14.4MB)
# 테스트 8 〉	통과 (472.49ms, 14.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)