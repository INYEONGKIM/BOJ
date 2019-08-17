input=__import__('sys').stdin.readline
r=0
for _ in range(int(input())):
    s=input().strip();r+=int(s[:-1])**int(s[-1])
print(r)
