n=int(input())
res=""
for j in range(1,n+1):
    n-=1
    cnt=0
    length=input()
    s=input()
    for i in s.split():
        if i=="sheep": cnt+=1
    res+="Case "+str(j)+": This list contains "+str(cnt)+" sheep.\n\n"
print(res,end="")
