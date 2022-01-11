def solution(number, k):
    answer = ''
    number = list(number)
    n = len(number)
    stack = []
    cnt = 0
    for num in number: # 앞자리 부터 결정!! 뒷자리 부터 X!
        while stack and cnt < k and num>stack[-1]:
            stack.pop()
            cnt+=1
        if len(stack)<n-k:
            stack.append(num)

    answer = "".join(stack)
    return answer

print(solution("1924",	2),	"94")
print(solution("1231234",	3),	"3234")
print(solution("4177252841",	4),	"775841")

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (0.14ms, 10.2MB)
# 테스트 5 〉	통과 (0.23ms, 10.2MB)
# 테스트 6 〉	통과 (8.63ms, 10.3MB)
# 테스트 7 〉	통과 (18.39ms, 11MB)
# 테스트 8 〉	통과 (27.47ms, 11.5MB)
# 테스트 9 〉	통과 (70.68ms, 16MB)
# 테스트 10 〉	통과 (192.35ms, 17.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.00ms, 10.2MB)