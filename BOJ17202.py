a=input();b=input();x=""
for i in range(8):
    x+=a[i]+b[i]
while len(x)>2:
    t=""
    for i in range(len(x)-1):
        t+=str((int(x[i])+int(x[i+1]))%10)
    x=t
print(x)
