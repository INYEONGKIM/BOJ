r=""
while True:
    t=input()
    if t=="#": break
    s=t.split()
    l=len(s)
    for i in range(l):
        r+=s[i][::-1]
        if i==l-1:
            r+="\n"
        else:
            r+=" "
print(r,end="")
