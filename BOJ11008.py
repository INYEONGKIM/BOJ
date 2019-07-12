n=int(input());res=""
for _ in range(n):
    s=input().split()
    ca=len(s[1]);r=0
    while s[0]!="":
        if len(s[0])<ca:
            r+=len(s[0])
            s[0]=""
        else:
            if s[0][:ca]==s[1]:
                s[0]=s[0][ca:]
            else:
                s[0]=s[0][1:]
            r+=1
    res+=str(r)+'\n'
print(res,end="")
