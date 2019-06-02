s=input();l=len(s);f=0;h=0;sa=0
for i in range(l):
    t=s[i]
    if f==0:
        if t==':': f=1
    elif f==1:
        if t=='-': f=2
        else: f=0
    elif f==2:
        if t==')': h+=1
        elif t=='(': sa+=1
        f=0
if h==0 and sa==0:
    print("none")
else:
    if h>sa: print("happy")
    elif h==sa: print("unsure")
    else: print("sad")
