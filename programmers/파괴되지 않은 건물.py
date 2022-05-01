def solution(board, skill):
    answer = 0
    
    tmp = [[0 for x in range(len(board[0])+1)] for x in range(len(board)+1)]
    
    #누적합 시작점
    for cur in skill:
        degree = cur[5]
        r1,c1,r2,c2 = cur[1],cur[2],cur[3],cur[4]
        #공격
        if cur[0] == 1:
            tmp[r1][c1] += -degree
            tmp[r1][c2+1] += degree
            tmp[r2+1][c1] += degree
            tmp[r2+1][c2+1] += -degree
        #회복
        else:
            tmp[r1][c1] += degree
            tmp[r1][c2+1] += -degree
            tmp[r2+1][c1] += -degree
            tmp[r2+1][c2+1] += degree
    # print(tmp)
    
    #누적합 구하기
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i][j+1]+=tmp[i][j]

    for j in range(len(tmp[0])-1):
        for i in range(len(tmp)-1):
            tmp[i+1][j]+=tmp[i][j]
    # print(tmp)
    
    #합계
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j]+=tmp[i][j]
            if board[i][j]>=1:
                answer += 1
    
    return answer