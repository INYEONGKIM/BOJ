n=int(input())
s=""
for i in range(n):
    n,c = map(int, input().split())
    if n%c==0:
        s=s+str(n//c) + "\n"
    else:
        s=s+str(n//c+1) + "\n"
print(s,end="")
