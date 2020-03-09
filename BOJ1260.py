from collections import defaultdict, deque
n, cnt, root = map(int,__import__('sys').stdin.readline().split())
d = defaultdict(list)
for _ in range(cnt):
    u,v=map(int,__import__('sys').stdin.readline().split())
    d[u].append(v)
    d[v].append(u)
for i in range(1,n+1):
    d[i].sort()

res=str(root)+' '
stk=deque(); stk.append(root)
visited = [False]*n; visited[root-1] = True
while stk:
    top = stk.pop()
    if not visited[top-1]:
        visited[top-1]=True
        res+=str(top)+' '
    for child in sorted(d[top], reverse=True):
        if not visited[child-1]:
            stk.append(child)
res=res.strip()
q=deque(d[root])
res+=f'\n{str(root)} '
visited=[False]*n
visited[root-1]=True
while q:
    l = len(q)
    for i in range(l):
        v = q.popleft()
        if not visited[v-1]:
            visited[v-1]=True
            res+=str(v)+' '
            for x in d[v]:
                if not visited[x-1]:
                    q.append(x)
print(res.strip())
