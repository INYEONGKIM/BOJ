import sys,math
r=""
while True:
    a,b=map(float,sys.stdin.readline().split())
    if a==0 and b==0: break
    r+=format((math.sqrt((a+b)*(a-b))/a),".3f")+'\n'
print(r,end="")
