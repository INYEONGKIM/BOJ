n=int(input());r=""
for i in range(1,n+1):
    a=[int(k) for k in input().split()]
    r+="Case "+str(i)+": "+str(sum(a))+'\n'
print(r,end="")
