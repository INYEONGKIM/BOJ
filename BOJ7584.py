r=""
def isfin(board):
    c=board[1][1]
    if c!='-' and ((board[0][0]==c==board[2][2]) or (board[2][0]==c==board[0][2]) or (board[0][1]==c==board[2][1]) or (board[1][0]==c==board[1][2])):
        return True, c
    for i in (0,2):
        if board[i][1]!='-' and (board[i][0]==board[i][1]==board[i][2]):
            return True, board[i][1]
    for i in (0,2):
        if board[1][i]!='-' and (board[0][i]==board[1][i]==board[2][i]):
            return True, board[1][i]
    return False, None

while True:
    board=[['-','-','-'],['-','-','-'],['-','-','-']]
    s=input().split()
    if s[0]=='#':
        break
    if s[0]=='X':
        for i in range(1,len(s)):
            x=int(s[i])-1
            if i%2==1:
                board[x//3][x%3]='X'
            else:
                board[x//3][x%3]='O'
    else:
        for i in range(1,len(s)):
            x = int(s[i])-1
            if i%2==1:
                board[x//3][x%3]='O'
            else:
                board[x//3][x%3]='X'
    f,w=isfin(board)
    if f:
        r+=w+'\n'
    else:
        r+='Draw\n'
print(r,end="")
