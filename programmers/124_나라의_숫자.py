def onetwofour(n,answer):
    if n <= 3:
        if n == 1:
            return "1"
        elif n == 2:
            return "2"
        elif n == 3:
            return "4"

    if n%3 != 0:
        tmp_n = (n//3+1)*3
    else:
        tmp_n = n
    diff = tmp_n-n
    
    answer += onetwofour(tmp_n//3-1, answer)
    
    if diff == 0:
        answer += "4"
    elif diff == 1:
        answer += "2"
    elif diff == 2:
        answer += "1"

    return answer

def solution(n):
    answer = ''
    if n%3 != 0:
        tmp_n = (n//3+1)*3
    else:
        tmp_n = n
    diff = tmp_n-n
    answer = onetwofour(tmp_n, answer)
    if diff > 0 :
        if diff == 1:
            answer = str(int(answer)-2)
        if diff == 2:
            answer = str(int(answer)-3)
    return answer

# solution(1)
# solution(2)
solution(3)
# solution(4)
# solution(5)
# solution(6)
# solution(7)
# solution(8)
# solution(9)
# solution(10)
# solution(11)
# solution(12)
# solution(13)
# solution(14)
# solution(15)
# solution(18)
# solution(21)
# solution(24)
# solution(27)
# solution(30)
# solution(33)
# solution(33)
# solution(513)
solution(500000000)