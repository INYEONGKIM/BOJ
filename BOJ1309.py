n = int(__import__('sys').stdin.readline())
if n == 1:
    print(3)
elif n == 2:
    print(7)
else:
    dp = [0]*n
    dp[0] = 3
    dp[1] = 7
    for i in range(2, n):
        dp[i] = (2*dp[i-1] + dp[i-2]) % 9901
    print(dp[-1])