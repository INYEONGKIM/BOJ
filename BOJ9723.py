import sys
r=""
for i in range(1,int(sys.stdin.readline())+1):
    a=[int(k) for k in sys.stdin.readline().split()];a.sort()
    if a[0]**2+a[1]**2==a[2]**2:
        r+="Case #"+str(i)+": YES\n"
    else:
        r+="Case #"+str(i)+": NO\n"
print(r,end="")
