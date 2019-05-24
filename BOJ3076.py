r,c=map(int,input().split());a,b=map(int,input().split());res=""
for i in range(r):
    t=""
    for j in range(c):
        if i%2==0:
            if j%2==0:
                t+='X'*b
            else:
                t+='.'*b
        else:
            if j%2==0:
                t+='.'*b
            else:
                t+='X'*b
    t+='\n'
    res+=t*a
print(res,end="")
