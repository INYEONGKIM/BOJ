a,b=map(str,input().split())
r=int(a[::-1].lstrip('0'))+int(b[::-1].lstrip('0'))
r=str(r)
print(r[::-1].lstrip('0'))
