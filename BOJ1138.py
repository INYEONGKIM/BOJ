n = int(__import__('sys').stdin.readline())
a = [int(_) for _ in __import__('sys').stdin.readline().split()]
res = [-1] * n
for i in range(n):
    for j in range(n):
        if a[j] > i:
            continue
        c = 0
        for front in range(i):
            if res[front] > j:
                c += 1
        if c == a[j]:
            res[i] = j+1
            break
print(' '.join(map(str, res)))
