# print("hello git")
a,b,c=map(int,input().split());r=1;m=a%c
while b>0:
    if b%2==1:
        r*=m
        r%=c
    m=(m%c*m%c)%c
    b//=2
print(r)
