import sys
r=0
for _ in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    r+=a*b
print(r)
