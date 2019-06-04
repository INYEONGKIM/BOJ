s=input();l=len(s)
if l==3:
    if s[1]=="0":
        print(int(s[:2])+int(s[2]))
    else:
        print(int(s[0])+int(s[1:]))
elif l==2:
    print(int(s[0])+int(s[1]))
else:
    print(20)
