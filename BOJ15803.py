x=[];y=[]
for _ in range(3):
    a,b=map(int,input().split())
    x.append(a);y.append(b)
print((x[0]*y[1]+x[1]*y[2]+x[2]*y[0]-(y[0]*x[1]+y[1]*x[2]+y[2]*x[0])) and "WINNER WINNER CHICKEN DINNER!" or "WHERE IS MY CHICKEN?")
