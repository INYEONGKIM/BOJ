n=int(input());a=0;b=0;c=0;d=0;e=0
for _ in range(n):
    x,y=map(int,input().split())
    if x==0:
        e+=1
    else:
        if y==0:
            e+=1
        else:
            if x>0:
                if y>0: a+=1
                else: d+=1
            else:
                if y<0: c+=1
                else: b+=1
print("Q1: ",a,"\nQ2: ",b,"\nQ3: ",c,"\nQ4: ",d,"\nAXIS: ",e,sep="")
