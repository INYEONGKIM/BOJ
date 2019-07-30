import math,sys
n,x,y=map(int,sys.stdin.readline().split());th=math.sqrt(x**2+y**2);r=""
for _ in range(n):
    if th>=int(sys.stdin.readline()):
        r+="DA\n"
    else:
        r+="NE\n"
print(r,end="")
