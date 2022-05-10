N,M = 0,0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(cur_x,cur_y,other_x,other_y,board):
    global dx,dy,N,M
    # 방문 할 수 없는 발판(이미 방문 했거나, 발판이 원래 없는) 인지 확인
    if board[cur_x][cur_y]==0:return 0
    res = 0
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        
        if 0<=nx<N and 0<=ny<M and board[nx][ny]!=0:
            board[cur_x][cur_y] = 0
            new_res = dfs(other_x,other_y,nx,ny,board)+1
            board[cur_x][cur_y] = 1
            #기존 지는 상태에서 이길 수있으면 이기는 경우로 교체
            if res%2==0 and new_res%2==1: res = new_res
            #기존 지는 상태에서 지는 경우가 새롭게 오면 더 오래 버틸 수 있는 경우로 교체
            elif res%2==0 and new_res%2==0: res = max(res,new_res)
            #기존 이기는 상태에서 이기는 경우가 새롭게 오면 더 빠른 경우로 교체
            elif res%2==1 and new_res%2==1: res = min(res,new_res)

    return res


def solution(board, aloc, bloc):
    global N,M
    answer = -1
    
    N = len(board)
    M = len(board[0])
    answer = dfs(aloc[0],aloc[1],bloc[0],bloc[1],board)
    return answer

solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2])