a,b=input().split();n=len(a);m=len(b)
ridx=-1;cidx=-1;f=False;r=""
for i in a:
    if not f:
        if i in b:
            f=True
            ridx=b.index(i)
            cidx=a.index(i)
for i in range(m):
    if i==ridx: r+=a+'\n'
    else:
        r+='.'*cidx+b[i]+'.'*(n-1-cidx)+'\n'
print(r,end="")
