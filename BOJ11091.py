n=int(input());res=""
for _ in range(n):
    a=[0]*26;t=""
    s=input().lower()
    for i in s:
        if 'a'<=i<='z':
            a[ord(i)-ord('a')]+=1
    for i in range(26):
        if a[i]==0:
            t+=chr(ord('a')+i)
    if len(t)==0:
        res+="pangram\n"
    else:
        res+="missing "+t+"\n"
print(res,end="")
