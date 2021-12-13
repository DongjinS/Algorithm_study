def solution(brown, yellow):
    from itertools import combinations
    mul_ans = brown + yellow
    a = yellow
    answer = []
    while True:
        #a 가 yellow의 약수인지
        if yellow % a == 0:
            b = yellow//a
            # a+2, b+2의 곱이 답과 맞고 a+2, b+2의 곱 - yellow가 brown인지
            if (a+2) * (b+2) == mul_ans and (a+2)*(b+2) - yellow == brown:
                answer.append(max(a+2,b+2))
                answer.append(min(a+2,b+2))
                break
        a -=1

    return answer
