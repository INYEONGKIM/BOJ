n=int(input())
memo = [0] * (n + 1)
for i in range(1, n+1):
    memo[i] = 1 + memo[i-1]
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2]+1)
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3]+1)
print(memo[n]-1)
