n=int(input());r=""
for _ in range(n):
    t=""
    a,b=map(int,input().split())
    s=input();l=len(s)
    for i in range(l):
        t+=chr(ord('A')+(a*(ord(s[i])-ord('A'))+b)%26)
    r+=t+'\n'
print(r,end="")
