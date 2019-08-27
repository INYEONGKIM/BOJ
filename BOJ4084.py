input=__import__('sys').stdin.readline
r=""
while True:
    a,b,c,d=map(int,input().split());cnt=0
    if a==0==b==c==d: break
    while not (a==b==c==d):
        cnt+=1
        t1=abs(a-b);t2=abs(b-c);t3=abs(c-d);t4=abs(d-a)
        a=t1;b=t2;c=t3;d=t4
    r+=str(cnt)+'\n'
print(r,end="")
