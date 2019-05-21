n=int(input());s=input().split()
r=0;stk=1;
for i in range(n):
    if s[i]=="1":
        r+=stk
        stk+=1
    else:
        stk=1
print(r)
