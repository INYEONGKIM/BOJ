d=[0,1,1,2,2,1,2,1];x=int(input())
if x%7==0:
    print(x//7)
else:
    for i in range(8,x+1):
        if i%7==0:
            d.append(i//7)
        else:
            d.append(min(d[i-5],d[i-2],d[i-1])+1)
    print(d[x])
