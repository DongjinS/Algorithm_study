def solution(prices):
    from collections import deque
    prices = deque(prices)
    answer = []
    
    while prices:
        i=0
        cur = prices.popleft()
        if not prices:
            answer.append(0)
            break
        else:
            for p in prices:
                i+=1
                if p<cur:
                    break
            answer.append(i)
    
    return answer

solution([1, 2, 3, 2, 3])