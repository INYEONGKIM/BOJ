n,m=map(int,input().split());r=""
for j in range(n):
    s=[int(k) for k in input().split()]
    for i in range(m):
        f=2126*s[3*i]+7152*s[3*i+1]+722*s[3*i+2]
        if 0<=f<510000:
            r+="#"
        elif 510000<=f<1020000:
            r+="o"
        elif 1020000<=f<1530000:
            r+="+"
        elif 1530000<=f<2040000:
            r+="-"
        else:
            r+='.'
    if j<n-1:
        r+="\n"
print(r,end="")
