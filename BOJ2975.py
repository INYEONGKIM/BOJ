r=""
while True:
    s=input()
    if s=="0 W 0": break
    t=s.split()
    a=int(t[0]); b=int(t[2])
    if t[1]=="W":
        if a-b<-200:
            r+="Not allowed\n"
        else:
            r+=str(a-b)+"\n"
    else:
        r+=str(a+b)+"\n"
print(r,end="")
