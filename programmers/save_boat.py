def solution(people, limit):
    from collections import deque
    people.sort()
    people = deque(people)
    cur_weight = 0
    cnt = 0
    while people:
        cur_weight = people.pop()
        for _ in range(2):
            if people and cur_weight+people[0]<=limit:
                cur_weight += people.popleft()
        cur_weight = 0
        cnt+=1
            
        
    answer = cnt
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (2.64ms, 10.4MB)
# 테스트 2 〉	통과 (2.60ms, 10.3MB)
# 테스트 3 〉	통과 (2.10ms, 10.3MB)
# 테스트 4 〉	통과 (1.68ms, 10.3MB)
# 테스트 5 〉	통과 (1.08ms, 10.3MB)
# 테스트 6 〉	통과 (0.74ms, 10.2MB)
# 테스트 7 〉	통과 (1.19ms, 10.2MB)
# 테스트 8 〉	통과 (0.09ms, 10.2MB)
# 테스트 9 〉	통과 (0.20ms, 10.3MB)
# 테스트 10 〉	통과 (2.01ms, 10.3MB)
# 테스트 11 〉	통과 (1.68ms, 10.2MB)
# 테스트 12 〉	통과 (1.49ms, 10.2MB)
# 테스트 13 〉	통과 (1.93ms, 10.2MB)
# 테스트 14 〉	통과 (1.85ms, 10.3MB)
# 테스트 15 〉	통과 (0.30ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (16.41ms, 10.7MB)
# 테스트 2 〉	통과 (20.41ms, 10.7MB)
# 테스트 3 〉	통과 (16.94ms, 10.7MB)
# 테스트 4 〉	통과 (19.12ms, 10.8MB)
# 테스트 5 〉	통과 (17.69ms, 10.7MB)


# 보트에 두명 만 탈 수 있는거 신경 안쓴 코드
def solution2(people, limit):
    from collections import deque
    people.sort()
    people = deque(people)
    cur_weight = 0
    cnt = 0
    while people:
        cur_weight = people.pop()
        while people and cur_weight+people[0]<=limit:
            cur_weight += people.popleft()
        cur_weight = 0
        cnt+=1
            
        
    answer = cnt
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (1.06ms, 10.3MB)
# 테스트 2 〉	통과 (0.65ms, 10.3MB)
# 테스트 3 〉	통과 (0.83ms, 10.3MB)
# 테스트 4 〉	통과 (0.67ms, 10.2MB)
# 테스트 5 〉	통과 (0.62ms, 10.2MB)
# 테스트 6 〉	통과 (0.21ms, 10.3MB)
# 테스트 7 〉	통과 (0.40ms, 10.2MB)
# 테스트 8 〉	통과 (0.05ms, 10.2MB)
# 테스트 9 〉	통과 (0.09ms, 10.2MB)
# 테스트 10 〉	통과 (0.87ms, 10.4MB)
# 테스트 11 〉	통과 (0.78ms, 10.4MB)
# 테스트 12 〉	통과 (0.90ms, 10.3MB)
# 테스트 13 〉	통과 (0.67ms, 10.3MB)
# 테스트 14 〉	통과 (1.25ms, 10.3MB)
# 테스트 15 〉	통과 (0.08ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (10.48ms, 10.7MB)
# 테스트 2 〉	통과 (9.95ms, 10.8MB)
# 테스트 3 〉	통과 (9.80ms, 10.8MB)
# 테스트 4 〉	통과 (9.90ms, 10.8MB)
# 테스트 5 〉	통과 (8.81ms, 10.7MB)
