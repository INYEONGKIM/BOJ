k = int(__import__('sys').stdin.readline())
a = [int(_) for _ in __import__('sys').stdin.readline().split()]
l = 2**k-1
res = ""
for i in range(k-1, -1, -1):
    idx = 2**i-1
    t = ""
    while idx < l:
        t += f'{a[idx]} '
        idx += 2**(i+1)
    res += f'{t}\n'
print(res, end="")
