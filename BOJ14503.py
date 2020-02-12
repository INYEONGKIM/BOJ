input = __import__('sys').stdin.readline
n,m=map(int, input().split())
x,y,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
res=0; cnt=0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
b_dx = [1, 0, -1, 0]
b_dy = [0, -1, 0, 1]

def dfs(x, y, d):
    global res
    if board[x][y] == 1:
        return
    if board[x][y]==0:
        board[x][y] = -1
        res += 1
    for i in range(4):
        f_d = (3 + d) % 4
        f_x = x + dx[f_d]
        f_y = y + dy[f_d]

        if board[f_x][f_y] == 0:
            dfs(f_x, f_y, f_d)
            return
        else:
            d = f_d
    f_x = x + b_dx[d]
    f_y = y + b_dy[d]
    dfs(f_x, f_y, d)
dfs(x, y, d)
print(res)
