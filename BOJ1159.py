a=[0]*26
for _ in range(int(input())):
    s=input()
    a[ord(s[0])-ord('a')]+=1
if max(a)<5:
    print("PREDAJA")
else:
    r=""
    for i in range(26):
        if a[i]>=5:
            r+=chr(ord('a')+i)
    print(r)
