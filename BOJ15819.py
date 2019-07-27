import sys
input=sys.stdin.readline
n,x=map(int,input().split());a=[]
for _ in range(n):
    a.append(input())
a.sort()
print(a[x-1],end="")
