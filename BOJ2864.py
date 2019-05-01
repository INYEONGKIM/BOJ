a,b=map(str,input().split())
a1=""; b1="";s=""
al=len(a); bl=len(b)
for i in range(al):
    if a[i]=="6":
        a1+="5"
    else:
        a1+=a[i]
for i in range(bl):
    if b[i]=="6":
        b1+="5"
    else:
        b1+=b[i]
s+=str(int(b1)+int(a1))+" "
a1=""; b1=""
for i in range(al):
    if a[i]=="5":
        a1+="6"
    else:
        a1+=a[i]
for i in range(bl):
    if b[i]=="5":
        b1+="6"
    else:
        b1+=b[i]
s+=str(int(b1)+int(a1))
print(s)
