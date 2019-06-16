s=input();f=True
try:
    while s!="":
        if s[0]=="p":
            t=s[:2]
            if t=="pi":
                s=s[2:]
            else:
                f=False; break
        elif s[0]=="k":
            t=s[:2]
            if t=="ka":
                s=s[2:]
            else:
                f=False; break
        elif s[0]=="c":
            t=s[:3]
            if t=="chu":
                s=s[3:]
            else:
                f=False; break
        else:
            f=False; break
except:
    f=False
if f:
    print("YES")
else:
    print("NO")
