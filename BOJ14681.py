x = int(__import__('sys').stdin.readline())
y = int(__import__('sys').stdin.readline())
if x > 0:
    print(1 if y > 0 else 4)
else:
    print(2 if y > 0 else 3)
