from typing import NewType


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(numbers)
    return str(int(answer))
solution([3, 30, 34, 5, 9])

#https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html