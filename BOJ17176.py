a=[0]*53;n=int(input());x=[int(i) for i in input().split()];s=input();f=True
for i in x:
    a[i]+=1
for i in s:
    if i==' ':
        a[0]-=1
    elif 'A'<=i<='Z':
        a[ord(i)-ord('A')+1]-=1
    else:
        a[ord(i)-ord('a')+27]-=1
for i in a:
    if i!=0:
        f=False;break
if f:
    print('y')
else:
    print('n')
