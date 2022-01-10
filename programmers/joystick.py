def solution(name):
    from collections import deque
    
    answer = 0
    name = list(name)
    init = ["A" for x in name]
    x = 0 #왼쪽이동
    y = 0 #오른쪽이동
    i = 0 #커서 이동 횟수
    visited = set()
    while init != name:
        if x not in visited and name[x] != "A":
            answer += i
            answer += min(ord(name[x])-ord("A"),(ord("Z")+1)-ord(name[x]))
            init[x] = name[x]
            visited.add(x)
            y = x #시작 위치 초기화
            i = 0
        elif y not in visited and name[y] != "A":
            answer += i
            answer += min(ord(name[y])-ord("A"),(ord("Z")+1)-ord(name[y]))
            init[y] = name[y]
            visited.add(y)
            x = y #시작 위치 초기화
            i = 0

        x+=1
        y-=1
        i += 1
    
    return answer

print(solution("JEROEN"),56)
print(solution("JAN"),23)
print(solution("ABAAB"),5)
print(solution("ABAAAAAAAAABB"), 7)
print(solution("JAZ"), 11)
print(solution("ZAAAZZZZZZZ"), 15)

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
