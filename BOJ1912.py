n = int(__import__('sys').stdin.readline())
dp = [int(_) for _ in __import__('sys').stdin.readline().split()]
for i in range(1, n):
    dp[i] = max(dp[i], dp[i]+dp[i-1])
print(max(dp))
