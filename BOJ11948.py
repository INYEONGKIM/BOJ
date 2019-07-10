s=0;a=[]
for _ in range(4):
    a.append(int(input()))
s+=sum(a)-min(a);a=[]
for _ in range(2):
    a.append(int(input()))
s+=sum(a)-min(a)
print(s)
