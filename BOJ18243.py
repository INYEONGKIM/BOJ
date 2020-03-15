from collections import deque
n, e = map(int, __import__('sys').stdin.readline().split())
g = [[False]*n for _ in range(n)]
for _ in range(e):
    a, b = map(int, __import__('sys').stdin.readline().split())
    g[a-1][b-1] = True
    g[b-1][a-1] = True

res = "Small World!"
for src in range(n):
    visit = [0]*n
    q = deque()

    for x in range(n):
        if g[src][x]:
            q.append((x, 1))
            visit[x] = 1

    while q:
        l = len(q)
        for _ in range(l):
            dst, depth = q.popleft()
            for x in range(n):
                if x != src and visit[x] == 0 and g[dst][x]:
                    q.append((x, depth+1))
                    visit[x] = depth+1
    if max(visit) > 6 or (0 in visit[:src] or 0 in visit[src+1:]):
        res = "Big World!"

print(res)
