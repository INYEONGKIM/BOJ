l=int(input());s=input();c=0
for i in s:
    if i=='S': c+=1
x=c+(l-c)//2+1;print((x>l) and l or x)
