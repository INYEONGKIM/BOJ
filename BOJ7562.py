input=__import__('sys').stdin.readline
r=""
for _ in range(int(input())):
    n=int(input());g=[[False]*n for _ in range(n)]
    x,y=map(int,input().split());g[x][y]=True
    dx,dy=map(int,input().split());c=0
    q=[(x,y,c)]
    while q!=[]:
        x,y,c=q.pop(0)
        if x==dx and y==dy: break
        for nx,ny in (x-2,y-1),(x-2,y+1),(x+2,y-1),(x+2,y+1),(x-1,y-2),(x-1,y+2),(x+1,y-2),(x+1,y+2):
            if nx<0 or ny<0 or nx>=n or ny>=n: continue
            if g[nx][ny]: continue
            g[nx][ny]=True
            q.append((nx,ny,c+1))
    r+=str(c)+'\n'
print(r,end="")
