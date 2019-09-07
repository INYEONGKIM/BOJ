l=[x for x in range(1,246913)];l.insert(0,1)
for i in range(2,246913):
    j=2
    while 246912>=i*j:
        l[i*j]=1;j+=1
r=""
while True:
    n=int(__import__('sys').stdin.readline())
    if n<=0:
        break
    c=0
    for i in l:
        if i!=1 and n<i and i<=2*n: c+=1
    r+=str(c)+'\n'
print(r,end="")
