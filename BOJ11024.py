res=""
n=int(input())
while n>0:
    n-=1
    a=[int(i) for i in input().split()]
    res+=(str(sum(a)) + "\n")
print(res,end="")
