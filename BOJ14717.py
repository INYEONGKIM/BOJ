d=[int(i)%10+1 for i in range(20)]
a,b=map(int,input().split());d.remove(a);d.remove(b);p=0
if a==b:
    for i in range(17):
        for j in range(i+1,18):
            if d[i]==d[j]>a:
                p+=1
else:
    th=(a+b)%10
    for i in range(17):
        for j in range(i+1,18):
            if d[i]==d[j] or th<=(d[i]+d[j])%10:
                p+=1
print(format(round(1-p/153,3),".3f"))
