n=int(__import__('sys').stdin.readline())
dp=[1]*90
for i in range(2,90):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n-1])
