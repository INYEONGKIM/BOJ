n=int(input())
t=n*(n+1)*(n+2)//6
for i in range(n-1,0,-2):
    t+=i*(i+1)//2
print(t)
