def rotate(cur, flag):
    _next = []
    if flag == 0:
        _next = [cur[0],cur[1]-1]
    elif flag == 1:
        _next = [cur[0]-1,cur[1]]
    elif flag == 2:
        _next = [cur[0],cur[1]+1]
    elif flag == 3:
        _next = [cur[0]+1,cur[1]]
    
    if flag >= 3:
        flag = 0
    else:
        flag+=1
        
    
    return [_next, flag]

def choose_next(cur, flag):
    _next = []
    if flag == 0:
        _next = [cur[0],cur[1]+1]
    elif flag == 1:
        _next = [cur[0]+1,cur[1]]
    elif flag == 2:
        _next = [cur[0],cur[1]-1]
    elif flag == 3:
        _next = [cur[0]-1,cur[1]]

    return _next

def solution(rows, columns, queries):
    answer = []
    targets = []
    matrix = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]
    
    for querie in queries:
        targets.append([(querie[0], querie[1]), (querie[2], querie[3])])
    
    for target in targets:
        lt = [min(target[0][0], target[1][0])-1, min(target[0][1], target[1][1])-1]
        rt = [min(target[0][0], target[1][0])-1, max(target[0][1], target[1][1])-1]
        lb = [max(target[0][0], target[1][0])-1, min(target[0][1], target[1][1])-1]
        rb = [max(target[0][0], target[1][0])-1, max(target[0][1], target[1][1])-1]

        start = lt
        cur = lt
        tmp_min = float('inf')
        _next = []
        flag = 0
        last_num = matrix[cur[0]][cur[1]]

        while True:
            tmp_min = min(tmp_min, matrix[cur[0]][cur[1]])
            cur_num = matrix[cur[0]][cur[1]]
            matrix[cur[0]][cur[1]] = last_num
            last_num = cur_num
            _next = choose_next(cur, flag)

            if _next[0]<lt[0] or _next[0]>lb[0] or _next[0]<0 or _next[0]>=rows or _next[1]<lt[1] or _next[1]>rt[1] or _next[1]<0 or _next[1]>=columns:
                _next,flag = rotate(_next, flag)
                _next = choose_next(cur, flag)

            if _next == start:
                matrix[_next[0]][_next[1]] = last_num
                break
            cur = _next
        answer.append(tmp_min)
    
    return answer

solution(	6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]] )