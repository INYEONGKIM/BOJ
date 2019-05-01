n=1000
s = [0, 0] + [1] * (n - 1)
for i in range(2, int(n**.5)+1):
    if s[i]:
        s[i*2::i] = [0] * ((n - i)//i)
l = [i for i, v in enumerate(s) if v]
size=int(input())
r=[int(i) for i in input().split()]
res=0
for i in r:
    if i in l:
        res+=1
print(res)
