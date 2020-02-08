n,m,x,y,c=map(int,__import__('sys').stdin.readline().split());board=[[] for _ in range(n)];res=''
for i in range(n):
    board[i]=list(map(int,__import__('sys').stdin.readline().split()))
dice=[0, 0, 0, 0, 0, 0];cmd=[int(i) for i in __import__('sys').stdin.readline().split()]
for i in range(c):
    if cmd[i]==1:
        if y<m-1:
            y+=1
            res+=str(dice[4])+'\n'
            if board[x][y]!=0:
                dice[3]=board[x][y]
                board[x][y]=0
            else:
                board[x][y]=dice[3]
            dice = [dice[4], dice[1], dice[2], dice[0], dice[5], dice[3]]
        else: continue
    elif cmd[i]==2:
        if y>0:
            y-=1
            res+=str(dice[3])+'\n'
            if board[x][y]!=0:
                dice[4]=board[x][y]
                board[x][y]=0
            else:
                board[x][y]=dice[4]
            dice = [dice[3], dice[1], dice[2], dice[5], dice[0], dice[4]]
        else: continue
    elif cmd[i]==3:
        if x>0:
            x-=1
            res+=str(dice[2])+'\n'
            if board[x][y]!=0:
                dice[1]=board[x][y]
                board[x][y]=0
            else:
                board[x][y]=dice[1]
            dice = [dice[2], dice[0], dice[5], dice[3], dice[4], dice[1]]
        else: continue
    else:
        if x<n-1:
            x+=1
            res+=str(dice[1])+'\n'
            if board[x][y]!=0:
                dice[2]=board[x][y]
                board[x][y]=0
            else:
                board[x][y]=dice[2]
            dice = [dice[1], dice[5], dice[0], dice[3], dice[4], dice[2]]
        else: continue
print(res,end='')
