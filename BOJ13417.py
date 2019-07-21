r=""
for _ in range(int(input())):
    x=int(input())
    a=input().split();s=a[0]
    for i in range(1,x):
        if a[i]<=s[0]:
            s=a[i]+s
        else:
            s+=a[i]
    r+=s+'\n'
print(r,end="")
