r=""
while True:
    s=input()
    if s=="0":
        break
    l=len(s)
    while l>=2:
        n=0
        for i in range(l):
            n+=int(s[i])
        s=str(n);l=len(s)
    r+=s+'\n'
print(r,end="")
