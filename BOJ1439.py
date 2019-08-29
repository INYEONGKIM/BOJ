s=input=__import__('sys').stdin.readline().strip();l=len(s)
a=s[0];cnt0=0;cnt1=0
if a=='0': cnt0+=1
else: cnt1+=1
for i in range(1,l):
    t=s[i]
    if t!=a:
        if t=='1': cnt1+=1
        else: cnt0+=1
    a=t
print(cnt0 if cnt0<cnt1 else cnt1)
