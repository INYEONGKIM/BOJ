al=[3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input();b = input();l=len(a);c=[]
for i in range(l):
    c.append(al[ord(a[i])-ord('A')])
    c.append(al[ord(b[i])-ord("A")])
for i in range(2*l-2):
    t=[]
    for j in range(len(c)-1):
        t.append((c[j]+c[j+1])%10)
    c=t
print(c[0],c[1],sep="")
