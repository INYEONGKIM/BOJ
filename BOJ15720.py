b,s,e=map(int,input().split())
bl=[int(i) for i in input().split()];sl=[int(i) for i in input().split()];el=[int(i) for i in input().split()]
bl.sort(reverse=True);sl.sort(reverse=True);el.sort(reverse=True)
print(sum(bl)+sum(sl)+sum(el));d=0;t=min(b,s,e)
for i in range(t):
    d+=0.9*(bl[i]+sl[i]+el[i])
d+=sum(bl[t:])+sum(sl[t:])+sum(el[t:])
print(int(d))
