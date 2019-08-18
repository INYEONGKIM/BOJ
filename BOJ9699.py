input=__import__('sys').stdin.readline
n=int(input());r=""
for k in range(1,n+1):
    a=[int(i) for i in input().split()]
    r+="Case #"+str(k)+": "+str(max(a))+'\n'
print(r.strip())
