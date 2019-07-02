s=input();le=len(s);v=[False]*le
def f(l,r):
    m='a';idx=-1
    for i in range(l,r):
        if not v[i] and (m>s[i]):
            m=s[i]
            idx=i
    if m=='a': return
    v[idx]=True
    for i in range(le):
        if v[i]:
            print(s[i],end='')
    print()
    f(idx+1,r)
    f(l,idx)
f(0,le)
