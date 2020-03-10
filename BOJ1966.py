from collections import deque
res=""
for _ in range(int(__import__('sys').stdin.readline())):
    rest = [0]*9
    q = deque()
    n,target=map(int, __import__('sys').stdin.readline().split())
    for idx, x in enumerate(map(int, __import__('sys').stdin.readline().split())):
        rest[x-1] += 1
        q.append((x,idx))
    found = False
    cnt = 0
    while not found:
        priority, idx = q.popleft()
        if priority==9:
            cnt += 1
            rest[8] -= 1
            if idx == target:
                found = True
                break
        else:
            if max(rest[priority:]) > 0:
                q.append((priority, idx))
            else:
                cnt += 1
                rest[priority - 1] -= 1
                if idx == target:
                    found = True
                    break
    res += f'{cnt}\n'
print(res, end="")
