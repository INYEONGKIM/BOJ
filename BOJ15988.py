res = ""
dp = [1]*10**6
dp[1] = 2
dp[2] = 4
for i in range(3, 10**6):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % (10**9+9)
for _ in range(int(__import__('sys').stdin.readline())):
    n = int(__import__('sys').stdin.readline())
    res += str(dp[n-1])+'\n'
print(res,end="")
