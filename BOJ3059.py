n=int(input());r=""
for _ in range(n):
    c=[False]*26;a=0
    s=input();l=len(s)
    for i in range(l):
        c[ord(s[i])-ord('A')]=True
    for i in range(26):
        if not c[i]:
            a+=i+65
    r+=str(a)+'\n'
print(r,end="")
