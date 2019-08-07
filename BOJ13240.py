b=['*','.']
c,r=map(int,input().split());res=""
for i in range(c):
    s=0
    if i%2==1: s=1
    for j in range(r):
        res+=b[s%2];s+=1
    res+='\n'
print(res,end="")
