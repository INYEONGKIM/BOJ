s=__import__('sys').stdin.readline().strip();r=0;n='A';l=len(s)
for i in range(l):
    if (ord(s[i])-ord(n)+26)%26<(ord(n)-ord(s[i])+26)%26:
        r+=(ord(s[i])-ord(n)+26)%26
    else:
        r+=(ord(n)-ord(s[i])+26)%26
    n=s[i]
print(r)
