import sys
r=""
while True:
    s=sys.stdin.readline().strip()
    if s=="#": break
    t="";f=True
    for i in s:
        if i=='b': t+='d'
        elif i=='d': t+='b'
        elif i=='p': t+='q'
        elif i=='q': t+='p'
        elif i=='i' or i=='o' or i=='v' or i=='w' or i=='x': t+=i
        else: f=False; break
    if f: r+=t[::-1]+'\n'
    else: r+='INVALID\n'
print(r,end="")
