r=""
while True:
    s=input(); cnt=0
    if s=="#": break
    x,a,t = s.partition(" ");
    t = t.lower(); tl=len(t)
    for i in range(tl):
        if t[i]==x: cnt+=1
    r+=x+" "+str(cnt)+"\n"
print(r)
