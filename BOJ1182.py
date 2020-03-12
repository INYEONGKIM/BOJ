n,target = map(int,__import__('sys').stdin.readline().split())
numbers=[int(_) for _ in __import__('sys').stdin.readline().split()]

def dfs(depth, r, s):
    if depth == n:
        if s is not "" and r == target:
            return 1
        else:
            return 0
    return dfs(depth+1, r, s) + dfs(depth+1, r+numbers[depth], s + str(numbers[depth]))

print(dfs(0, 0, ""))
