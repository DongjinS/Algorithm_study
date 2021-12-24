#https://dong-co.tistory.com/65 #답 찾아보았습니다..ㅠㅠ
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    lp = 0
    rp = distance
    mid = (lp+rp)//2
    while lp<=rp:
        prev_rock = 0
        remove_cnt = 0
        tmp_min = float('inf')
        for rock in rocks:
            if rock - prev_rock<mid:
                remove_cnt += 1
            else:
                tmp_min = min(tmp_min, rock - prev_rock)
                prev_rock = rock
        
        if remove_cnt > n:
            rp = mid - 1
        else:
            answer = tmp_min
            lp = mid + 1
            
        mid = (lp+rp)//2
        
    return answer

# 테스트 1 〉	통과 (0.33ms, 10.3MB)
# 테스트 2 〉	통과 (0.28ms, 10.3MB)
# 테스트 3 〉	통과 (0.24ms, 10.3MB)
# 테스트 4 〉	통과 (17.24ms, 10.3MB)
# 테스트 5 〉	통과 (14.24ms, 10.4MB)
# 테스트 6 〉	통과 (137.93ms, 12.2MB)
# 테스트 7 〉	통과 (227.25ms, 12.2MB)
# 테스트 8 〉	통과 (229.15ms, 12.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.4MB)