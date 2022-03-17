def solution(numbers):
    answer = 0

    numbers.sort(reverse=True)
    print(numbers)

    cur = numbers.pop()
    for i in range(10):
        if cur == i:
          if numbers:
            cur = numbers.pop()
        else:
          answer += i
    
    print(answer)
    return answer

solution([1, 2, 3, 4, 6, 7, 8, 0])
