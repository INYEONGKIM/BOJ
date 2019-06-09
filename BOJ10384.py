n=int(input());r=""
for k in range(1,n+1):
    a=[0]*26;s=input().upper();l=len(s)
    for i in range(l):
        if 0<=ord(s[i])-ord('A')<26:
            a[ord(s[i])-ord('A')]+=1
    if min(a)==0:
        r+="Case "+str(k)+": Not a pangram\n"
    elif min(a)==1:
        r+="Case "+str(k)+": Pangram!\n"
    elif min(a)==2:
        r+="Case "+str(k)+": Double pangram!!\n"
    elif min(a)==3:
        r+="Case "+str(k)+": Triple pangram!!!\n"
print(r,end="")
