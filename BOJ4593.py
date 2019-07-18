r=""
while True:
    a=input();b=input()
    if a==b=="E":
        break
    l=len(a);ac=0;bc=0
    for i in range(l):
        if a[i]=='S':
            if b[i]=='P':
                ac+=1
            elif b[i]=='R':
                bc+=1
        elif a[i]=='R':
            if b[i]=='S':
                ac+=1
            elif b[i]=='P':
                bc+=1
        else:
            if b[i]=='R':
                ac+=1
            elif b[i]=='S':
                bc+=1
    r+="P1: "+str(ac)+"\nP2: "+str(bc)+"\n"
print(r,end="")
