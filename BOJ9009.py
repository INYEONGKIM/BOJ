f = [0] * 50
f[1] = 1
for i in range(2, 50):
    f[i] = f[i-1] + f[i-2]

res = ""
for _ in range(int(__import__('sys').stdin.readline())):
    idx = 49
    x = -1
    target = int(__import__('sys').stdin.readline())
    for i in range(idx, 0, -1):
        if f[i] <= target:
            idx = i
            x = f[i]
            break
    r = f"{x}"
    while x != target:
        if target >= x + f[idx]:
            x += f[idx]
            r = f'{f[idx]} ' + r
        idx -= 1
    res += r + '\n'

print(res, end="")
