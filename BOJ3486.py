import sys
r=""
for _ in range(int(sys.stdin.readline())):
    a,b=sys.stdin.readline().split()
    r+=str(int(str(int(a[::-1])+int(b[::-1]))[::-1]))+'\n'
print(r,end="")
