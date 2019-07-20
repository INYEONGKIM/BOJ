r=""
for _ in range(int(input())):
    c=0;v=0
    s=input()
    for i in s:
        if i!=' ':
            if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
                v+=1
            else:
                c+=1
    r+=str(c)+' '+str(v)+'\n'
print(r,end="")
