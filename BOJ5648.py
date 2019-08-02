import sys
input=sys.stdin.readline
a=list(map(str,input().split()));n=int(a[0]);cnt=len(a)-1;b=[]
for i in range(1,cnt+1):
    b.append(int(a[i][::-1]))
while n!=cnt:
    t=input().split()
    for i in t:
        b.append(int(i[::-1]))
        cnt+=1
        if cnt==n: break
b.sort();r=""
for i in b:
    r+=str(i)+'\n'
print(r,end="")
