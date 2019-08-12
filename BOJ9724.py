import sys
input=sys.stdin.readline
n=int(input());r=""
for i in range(n):
    a,b=map(int,input().split());a=a**(1.0/3.0);b=int(b**(1.0/3.0))
    if a-int(a)==0.0: a=int(a)
    else: a=int(a)+1
    r+="Case #"+str(i+1)+": "+str(b-a+1)+'\n'
print(r,end="")
