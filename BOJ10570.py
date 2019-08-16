import sys
input=sys.stdin.readline
r=""
for _ in range(int(input())):
    a=[0]*1000
    for _ in range(int(input())):
        a[int(input())-1]+=1
    r+=str(a.index(max(a))+1)+'\n'
print(r.strip())
