n, m, k = map(int, __import__('sys').stdin.readline().split())
dp = [[0]*m for _ in range(n)]
if k == 0:
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[0][j] = 1
            else:
                if j == 0:
                    dp[i][0] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
else:
    stop_x, stop_y = (k - 1) // m, (k - 1) % m
    for i in range(stop_x + 1):
        for j in range(stop_y + 1):
            if i == 0:
                dp[0][j] = 1
            else:
                if j == 0:
                    dp[i][0] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    for i in range(stop_x, n):
        for j in range(stop_y, m):
            if i == stop_x:
                dp[i][j] = dp[stop_x][stop_y]
            else:
                if j == stop_y:
                    dp[i][j] = dp[stop_x][stop_y]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[n-1][m-1])
