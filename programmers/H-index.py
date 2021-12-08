def solution(citations):
    answer = len(citations)
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
        
    return answer

print(solution([3, 0, 6, 1, 5]))

#https://yunaaaas.tistory.com/56