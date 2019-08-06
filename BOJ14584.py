s=input();a=[];f=False
for _ in range(int(input())):
    a.append(input())
for i in range(26):
    t=list(s);l=""
    for x in t:
        z=ord(x)+1
        if chr(z)>'z':
            z-=26
        l+=chr(z)
    for k in a:
        if k in l:
            print(l);f=True;break
    if f: break
    s=l
