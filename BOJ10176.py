n=int(input())
res=""
for _ in range(n):
    r = [0] * 13
    s=input()
    l = len(s)
    for i in range(l):
        if 'a'<=s[i]<='m':
            r[ord(s[i])-ord('a')]+=1
        elif 'n'<=s[i]<='z':
            r[ord(s[i]) - ord('n')] -= 1
        elif 'A'<=s[i]<='M':
            r[ord(s[i]) - ord('A')] += 1
        elif 'N'<=s[i]<='Z':
            r[ord(s[i]) - ord('N')] -= 1
    if sum(r)==0:
        res+="Yes\n"
    else:
        res+="No\n"
print(res,end="")
