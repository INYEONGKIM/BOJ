m,n=map(int,input().split());p=[int(i) for i in input().split()];st=[-1,-1]
for _ in range(n):
    s=input().split();po=0
    for i in range(m):
        if s[i+1]=='O':
            po+=p[i]
    if st[1]<po:
        st=[int(s[0]),po]
    elif st[1]==po:
        if st[0]==-1 or st[0]>int(s[0]):
            st=[int(s[0]),po]
print(st[0],st[1])
