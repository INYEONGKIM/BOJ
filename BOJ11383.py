x,y=map(int,input().split());s=[];f=True
for _ in range(x):
    s.append(input())
for i in range(x):
    z=input()
    for j in range(y):
        if z[2*j]!=z[2*j+1] or z[2*j]!=s[i][j]:f=False
if f: print("Eyfa")
else: print("Not Eyfa")
