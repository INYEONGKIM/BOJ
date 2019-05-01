s,n=map(int, input().split())
a = [False,False] + [True]*(n-1)
primes=[]
res=""
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
    if i>=s: res+=str(i)+"\n"
print(res,end='')
