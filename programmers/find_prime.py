def search_prime(i: int) -> int: 
    if i > 2 :
        for divisor in range(2,i):
            #소수 아님
            if i%divisor == 0:
                return False
            #소수
            else:
                prime = 1
        if prime == 1:
            return True
    elif i == 2:
        return True

def solution(numbers):
    from itertools import permutations
    numbers = list(numbers)
    answer_set = set()
    
    for i in range(1,len(numbers)+1):
        candidatie = list(permutations(numbers,i))
        # candidatie 소수 있으면 answer += 1
        for chk in candidatie:
            chk = ''.join(chk)
            if search_prime(int(chk)):
                while chk[0] == "0":
                    chk = chk[1:]
                answer_set.add(chk)
    answer = len(answer_set)
    return answer

solution("011")