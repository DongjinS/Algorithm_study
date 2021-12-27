def dfs(numbers,i,total,target,answer):
    if i == len(numbers)-1 and total == target:
        return 1
    elif i == len(numbers)-1:
        return 0
    else:
        answer = dfs(numbers,i+1,total+numbers[i+1],target,answer) 
        answer += dfs(numbers,i+1,total-numbers[i+1],target,answer)
        return answer

def solution(numbers, target):
    answer = 0
    total = 0
    answer = dfs(numbers,-1,total,target,answer)
    print(answer)
    return answer

solution([1,1,1,1,1],3)