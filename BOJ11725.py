from collections import deque, defaultdict
n = int(__import__('sys').stdin.readline())
visited = [False] * (n+1)
dic = defaultdict(deque)
for _ in range(n-1):
    a, b = map(int, __import__('sys').stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
r = [0]*(n+1)
q = deque()
q.append((dic[1], 1))
visited[1] = True

while q:
    link, p = q.popleft()
    for l in link:
        if not visited[l]:
            visited[l] = True
            r[l] = p
            q.append((dic[l], l))
print('\n'.join(map(str, r[2:])))
