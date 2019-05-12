n=int(input())
res=""
for i in range(1,n+1):
    a,b=map(int, input().split())
    if a>=0:
        res+="Scenario #"+str(i)+":\n"+str((a+b)*(b-a+1)//2)
    elif a<0 and b>=0:
        res+="Scenario #"+str(i)+":\n"+str(b*(b+1)//2 + a*(abs(a)+1)//2)
    else:
        res+="Scenario #"+str(i)+":\n"+str((a+b)*(b-a+1)//2)
    if i!=n: res+="\n\n"
print(res,end="")
