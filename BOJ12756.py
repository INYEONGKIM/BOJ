a=[int(i) for i in input().split()];b=[int(i) for i in input().split()]
c=b[1]//a[0];d=a[1]//b[0]
if b[1]%a[0]>0:
    c+=1
if a[1]%b[0]>0:
    d+=1
if c==d:
    print("DRAW")
elif c<d:
    print("PLAYER A")
else:
    print("PLAYER B")
