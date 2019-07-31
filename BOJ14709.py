n=int(input());f=True
if n!=3: f=False
a=set()
for _ in range(n):
    b,c=map(int,input().split())
    a.add(b);a.add(c)
if a!={1,3,4}:
    f=False
print((f) and 'Wa-pa-pa-pa-pa-pa-pow!' or 'Woof-meow-tweet-squeek')
