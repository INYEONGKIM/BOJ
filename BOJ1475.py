l=[0,0,0,0,0,0,0,0,0]
s=input()
for i in range(len(s)):
    if s[i]=='9':
        l[6]+=1
    else:
        l[int(s[i])]+=1
if l[6]%2==1:
    l[6]+=1
l[6] = l[6]//2
print(max(l))
