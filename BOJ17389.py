input=__import__('sys').stdin.readline;n=int(input());s=input();t=0;b=0
for i in range(n):
    if s[i]=='O': t+=i+1+b;b+=1
    else: b=0
print(t)
