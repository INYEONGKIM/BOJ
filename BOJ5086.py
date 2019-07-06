r=""
while True:
    s=input().strip()
    if s=="0 0": break
    a,b=map(int,s.split())
    if a>b:
        if a%b==0:
            r+="multiple\n"
        else:
            r+="neither\n"
    else:
        if b%a==0:
            r+="factor\n"
        else:
            r+="neither\n"
print(r,end="")
