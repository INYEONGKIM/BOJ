input=__import__('sys').stdin.readline
r="";c=1
while True:
    n=int(input())
    if n==0: break
    r+=str(c)+'\n';c+=1
    a=[input().strip() for _ in range(n)]
    a.sort()
    r+='\n'.join(a)
    r+='\n'
print(r.strip())
