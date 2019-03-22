n=int(input())
k=[]
l=[]
for i in range(1,n+1):
    k.append(i)

while len(k)>1:
    l.append(k[0])
    del k[0]
    k.append(k[0])
    del k[0]
l.append(k[0])
for i in range(n):
    print(l[i]," ",sep="", end="")
