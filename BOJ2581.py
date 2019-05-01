a=int(input())
n=int(input())
s = [0, 0] + [1] * (n - 1)
for i in range(2, int(n**.5)+1):
    if s[i]:
        s[i*2::i] = [0] * ((n - i)//i)
p=[i for i, v in enumerate(s) if v]
sum=0; m=100001
for i in range(a,n+1):
    if i in p:
        sum+=i
        if m>i:
            m=i
if sum==0:
    print(-1)
else:
    print(sum, m,sep="\n")
