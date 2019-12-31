r="";k=int(input())
for _ in range(k):
    n,m=map(int,input().split())
    if n<12 or m<4: r+="-1\n"
    else: r+=str(m*11+4)+'\n'
print(r,end="")
