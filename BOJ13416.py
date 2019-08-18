input=__import__('sys').stdin.readline
r=""
for _ in range(int(input())):
    t=0
    for _ in range(int(input())):
        a=[int(i) for i in input().split()]
        if max(a)>0:
            t+=max(a)
    r+=str(t)+'\n'
print(r.strip())
