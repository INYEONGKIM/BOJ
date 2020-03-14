s = __import__('sys').stdin.readline().strip()
n = len(s)
res = 0
if n == 1:
    res = 1
else:
    s = '#'.join(s)
    new_n = 2*n -1

    def go(idx):
        i = 0
        while i+idx < new_n:
            if not ((idx + i) % 2 == 1) and s[idx+i] != s[new_n-i-1]:
                return False
            i += 1
        return True

    for j in range(new_n):
        if go(j):
            res = n + j//2
            break
print(res)
