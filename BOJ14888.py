n = int(__import__('sys').stdin.readline())
a = [int(_) for _ in __import__('sys').stdin.readline().split()]
plus, minus, mul, div = map(int, __import__('sys').stdin.readline().split())
max_val = -1000000001
min_val = 1000000001

def dfs(val, depth, plus, minus, mul, div):
    if depth == n:
        global max_val, min_val
        max_val = max(val, max_val)
        min_val = min(val, min_val)
        return
    else:
        if plus > 0:
            dfs(val+a[depth], depth + 1, plus - 1, minus, mul, div)

        if minus > 0:
            dfs(val-a[depth], depth + 1, plus, minus - 1, mul, div)

        if mul > 0:
            dfs(val*a[depth], depth + 1, plus, minus, mul - 1, div)

        if div > 0:
            if val < 0:
                dfs(-((-val) // a[depth]), depth + 1, plus, minus, mul, div - 1)
            else:
                dfs(val//a[depth], depth + 1, plus, minus, mul, div - 1)

dfs(a[0], 1, plus, minus, mul,div)
print(max_val, min_val, sep='\n')
