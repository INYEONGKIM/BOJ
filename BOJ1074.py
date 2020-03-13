n,r,c = map(int, __import__('sys').stdin.readline().split())
def dfs(n, r, c, add_num):
    if n <= 2:
        if r == 0:
            if c == 0:
                print(add_num)
                return
            else:
                print(add_num+1)
                return
        else:
            if c == 0:
                print(add_num+2)
                return
            else:
                print(add_num+3)
                return
    else:
        if r < n // 2:
            if c < n // 2:
                dfs(n//2, r, c, add_num)
            else:
                dfs(n//2, r, c - n//2, add_num + (n//2)**2)
        else:
            if c < n // 2:
                dfs(n//2, r - n//2, c, add_num + 2*((n//2)**2))
            else:
                dfs(n//2, r - n//2, c - n//2, add_num + 3*((n//2)**2))
dfs(2**n, r, c, 0)
