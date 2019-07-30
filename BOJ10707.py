a=[]
for _ in range(5):
    a.append(int(input()))
x=a[0]*a[4]
y=a[1]
if a[4]-a[2]>0:
    y+=(a[4]-a[2])*a[3]
print((x<y) and x or y)
