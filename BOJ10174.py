n=int(input())
res=""
for _ in range(n):
    s=input()
    l=len(s)
    flag=True
    for i in range(l//2+1):
        if i<=l-i-1:
            if 'A'<=s[i]<='Z' and 'a'<=s[l-i-1]<='z':
                t=s[i].lower()
            elif 'A'<=s[l-i-1]<='Z' and 'a'<=s[i]<='z':
                t=s[i].upper()
            else:
                t=s[i]
            if t!=s[l-i-1]:
                flag=False
                break
    if flag: res+="Yes\n"
    else: res+="No\n"
print(res,end="")
