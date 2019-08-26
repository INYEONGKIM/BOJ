input=__import__('sys').stdin.readline
r=""
while True:
    a,b=input().split()
    if a=="00:00"==b: break
    x,y=map(int,a.split(':'));t=y;t+=60*x
    x,y=map(int,b.split(':'));t+=x*60+y
    d=t//(24*60);t%=24*60
    if t//60<10: r+='0'
    r+=str(t//60)+':'
    if t%60<10: r+='0'
    r+=str(t%60)
    if d>0: r+=' +'+str(d)
    r+='\n'
print(r,end="")
