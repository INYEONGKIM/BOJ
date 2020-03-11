n=int(__import__('sys').stdin.readline())
budgets = list(map(int,__import__('sys').stdin.readline().split()))
M = int(__import__('sys').stdin.readline())
res = 0
if sum(budgets) <= M:
    res = max(budgets)
else:
    left = 0
    right = max(budgets)
    while left <= right:
        mid = (left+right)//2
        tot = 0
        for i in range(n):
            tot += min(mid, budgets[i])
        if tot <= M:
            if mid > res:
                res = mid
            left = mid + 1
        else:
            right = mid -1
print(res)
