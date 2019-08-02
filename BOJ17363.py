n,m=map(int,input().split());a=[];res=""
for _ in range(n):
    a.append(list(input()))
for i in range(m):
    r=""
    for j in range(n):
        t=a[j][i]
        if t=='-':
            r+='|'
        elif t=='|':
            r+='-'
        elif t=='/':
            r+='\\'
        elif t=='\\':
            r+='/'
        elif t=='^':
            r+='<'
        elif t=='<':
            r+='v'
        elif t=='v':
            r+='>'
        elif t=='>':
            r+='^'
        else:
            r+=t
    r+='\n'
    res=r+res
print(res,end="")
