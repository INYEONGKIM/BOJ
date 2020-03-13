def hanoi(depth, a, b, c):
    if depth == 1:
        print(a, c)
    else:
        hanoi(depth-1, a, c, b)
        print(a, c)
        hanoi(depth-1, b, a, c)
n=int(__import__('sys').stdin.readline())
print(2**n-1)
if n<=20:
    hanoi(n, 1, 2, 3)
