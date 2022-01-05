# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.
def solution(N, number):
    if N==number:
        return 1
    
    possible_num = [set() for x in range(9)]
    for i in range(1,9):
        print(possible_num)
        for j in range(i):
            for op1 in possible_num[j]:
                for op2 in possible_num[i-j]:
                    print(i,j, i-j)
                    possible_num[i].add(op1+op2)
                    possible_num[i].add(op1-op2)
                    possible_num[i].add(op1*op2)
                    if op2 != 0:
                        possible_num[i].add(op1//op2)
        possible_num[i].add(int(str(N)*i))
        if number in possible_num[i]:
            print(i)
            return i
                
    answer = -1
    return answer

solution(5,12)

# 테스트 1 〉	통과 (0.30ms, 10.5MB)
# 테스트 2 〉	통과 (0.01ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (15.78ms, 11.4MB)
# 테스트 5 〉	통과 (4.99ms, 10.7MB)
# 테스트 6 〉	통과 (0.17ms, 10.4MB)
# 테스트 7 〉	통과 (0.10ms, 10.4MB)
# 테스트 8 〉	통과 (9.54ms, 11.3MB)
# 테스트 9 〉	통과 (0.00ms, 10.5MB)