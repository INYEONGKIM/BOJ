input=__import__('sys').stdin.readline
n=int(input());visited=[False]*(n+1);a=[[] for _ in range(n+1)]
for _ in range(int(input())):
    x,y,c=map(int,input().split())
    a[x].append([c,y])
    a[y].append([c,x])
import heapq
q=[];visited[1]=True;cost=0;cnt=1
for i in a[1]: heapq.heappush(q,i)
while q:
    c,v=heapq.heappop(q)
    if not visited[v]:
        visited[v]=True;cnt+=1;cost+=c
        for i in a[v]: heapq.heappush(q,i)
    if cnt==n: break
print(cost)
