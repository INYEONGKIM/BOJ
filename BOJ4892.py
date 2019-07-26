import sys
input=sys.stdin.readline
r="";cnt=0
while True:
    cnt+=1
    x=int(input())
    if x==0:
        break
    x*=3
    t=-1
    if x%2==0:
        r+=str(cnt)+'. even '
        t=(3*(x//2))//9
    else:
        r+=str(cnt)+'. odd '
        t=(3*((x+1)//2))//9
    r+=str(t)+'\n'
print(r,end="")
