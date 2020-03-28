n = int(__import__('sys').stdin.readline())
if n == 1:
    print(int(__import__('sys').stdin.readline()))
elif n == 2:
    print(int(__import__('sys').stdin.readline()) + int(__import__('sys').stdin.readline()))
else:
    wine = [0] * n
    dp = [0] * n
    wine[0] = int(__import__('sys').stdin.readline())
    wine[1] = int(__import__('sys').stdin.readline())
    dp[0] = wine[0]
    dp[1] = wine[1] + wine[0]
    for i in range(2, n):
        wine[i] = int(__import__('sys').stdin.readline())
        dp[i] = max(dp[i-1], wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2])
    print(dp[-1])
