a=[0]*32
for _ in range(int(__import__('sys').stdin.readline())):
    s,e=map(int,__import__('sys').stdin.readline().split())
    for i in range(s,e):
        a[i]+=1
if max(a)<=int(__import__('sys').stdin.readline()): print(1)
else: print(0)
