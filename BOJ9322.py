class f:
    def __init__(self,s,i):
        self.s=s;self.i=i
r=""
for _ in range(int(__import__('sys').stdin.readline())):
    n=int(__import__('sys').stdin.readline())
    a=__import__('sys').stdin.readline().split()
    b=__import__('sys').stdin.readline().split()
    o=[-1]*n
    for i in range(n):
        for j in range(n):
            if b[i]==a[j]:
                o[i]=j;break
    t=""
    c=__import__('sys').stdin.readline().split()
    for i in range(n):
        o[i]=f(c[i],o[i])
    o.sort(key=lambda x:x.i)
    for x in o:
        t+=x.s+' '
    r+=t+'\n'
print(r,end="")
