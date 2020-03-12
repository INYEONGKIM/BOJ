res = ""
for _ in range(int(__import__('sys').stdin.readline())):
    n=int(__import__('sys').stdin.readline())
    a = []
    a.append([int(_) for _ in __import__('sys').stdin.readline().split()])
    a.append([int(_) for _ in __import__('sys').stdin.readline().split()])
    if n == 1:
        res = str(max(a))+'\n'
    elif n==2:
        res = str(max(a[0][0]+a[1][1], a[0][1]+a[1][0]))+'\n'
    else:
        a[0][1] += a[1][0]
        a[1][1] += a[0][0]
        for i in range(2, n):
            a[0][i] += max(a[1][i-2], a[1][i-1])
            a[1][i] += max(a[0][i-2], a[0][i-1])
        res += str(max(a[0][n-1], a[1][n-1])) + '\n'
print(res, end="")
