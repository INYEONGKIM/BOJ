n=int(input());s=input();t=s[0];f=True
for i in range(1,2*n):
    if t!=s[i]:
        t=s[i]
    else: f=False;break
if f: print("Yes")
else: print("No")
