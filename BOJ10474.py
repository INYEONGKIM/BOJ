input=__import__('sys').stdin.readline
r=""
while True:
    a,b=map(int,input().split())
    if a==0==b: break
    r+=str(a//b)+' '+str(a%b)+' / '+str(b)+'\n'
print(r.strip())
