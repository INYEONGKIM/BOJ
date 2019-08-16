import sys,math
r="";k=1
while True:
    a,b,c=map(int,sys.stdin.readline().split());f=True
    if a==0==b==c: break
    if c==-1:
        c=math.sqrt(a**2+b**2)
        t='c';v=c
    elif b==-1:
        if c<=a: f=False
        else:
            b=math.sqrt(c**2-a**2)
        t='b';v=b
    else:
        if c<=b: f=False
        else:
            a=math.sqrt(c**2-b**2)
        t='a';v=a
    if f and c<=a+b:
        r+="Triangle #" + str(k) + "\n"+t+" = " + format(v, ".3f") + '\n\n'
    else:
        r += "Triangle #" + str(k) + "\nImpossible.\n\n"
    k+=1
print(r.strip())
