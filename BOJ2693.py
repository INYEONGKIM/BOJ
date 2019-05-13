n=int(input())
res=""
for _ in range(n):
    l = [int(i) for i in input().split()]
    l.sort()
    res+=str(l[-3])+"\n"
print(res,end="")
