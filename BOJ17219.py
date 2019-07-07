a,b=map(int,input().split());d={};r=""
for _ in range(a):
    k,v=input().split()
    d[k]=v
for _ in range(b):
    r+=d[input()]+'\n'
print(r,end="")
