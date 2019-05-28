l=[]
for _ in range(7):
    a=int(input())
    if a%2==1:
        l.append(a)
if l==[]:
    print(-1)
else:
    print(sum(l),min(l),sep="\n")
