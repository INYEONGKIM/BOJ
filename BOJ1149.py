n = int(__import__('sys').stdin.readline())
dp = [[0]*3 for _ in range(n)]
for i in range(n):
    dp[i][0], dp[i][1], dp[i][2] = map(int, __import__('sys').stdin.readline().split())

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][0] += min(dp[i-1][1:])
        elif j == 1:
            dp[i][1] += min(dp[i-1][0], dp[i-1][2])
        else:
            dp[i][2] += min(dp[i-1][:-1])
print(min(dp[-1]))
