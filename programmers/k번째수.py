def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]-1
        end = command[1]
        target = command[2]-1
        tmp = array[start:end]
        tmp.sort()
        answer.append(tmp[target])
    return answer