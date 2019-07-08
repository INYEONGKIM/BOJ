a=input().split();r=5000
for i in a:
    if i=='1':
        r-=500
    elif i=='2':
        r-=800
    else:
        r-=1000
print(r)
