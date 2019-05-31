n=int(input());r=""
for _ in range(n):
    s=[int(i) for i in input().split()]
    s.sort()
    if abs(s[1]-s[-2])>=4:
        r+="KIN\n"
    else:
        r+=str(sum(s[1:4]))+"\n"
print(r)
