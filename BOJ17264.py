w=[]
n,p=map(int,input().split());f=False;u,d,th=map(int,input().split())
for _ in range(p):
    s=input().split()
    if s[1]=='W':
        w.append(s[0])
p=0
for _ in range(n):
    x=input()
    if x in w:
        p+=u
        if p>=th:
            f=True;break
    else:
        p-=d
        if p<0:
            p=0
if f:
    print("I AM NOT IRONMAN!!")
else:
    print("I AM IRONMAN!!")
