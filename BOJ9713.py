n=int(input())
res=""
for _ in range(n):
    sum=0
    x=int(input())
    for i in range(1,x+1):
        if i%2==1: sum+=i
    res+=str(sum)+"\n"
print(res,end="")
