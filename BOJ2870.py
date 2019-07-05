n=int(input());res="";a=[]
for _ in range(n):
    s=input();t=""
    for i in s:
        if '0'<=i<='9':
            t+=i
        else:
            if t!='':
                a.append(int(t))
            t=""
    if t!="":
        a.append(int(t))
t=sorted(a)
for i in t:
    res+=str(i)+'\n'
print(res,end="")
