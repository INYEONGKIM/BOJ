s=input();r=0;sl=len(s)
for i in range(sl):
    r+=(ord(s[i])-ord('A')+1)*26**(sl-i-1)
print(r)
