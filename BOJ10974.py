def dfs(s, depth):
    if depth==n:
        print(" ".join(s))
        return
    else:
        for j in range(1, n+1):
            if str(j) not in s:
                dfs(s+str(j), depth+1)

n=int(__import__('sys').stdin.readline())
for i in range(1, n+1):
    dfs(str(i), 1)
