x=input()
x16=x+"0000"
x="0000"+x
c=0
res=""
j = len(x16)
for i in range(j):
    if x[j-i-1]==x16[j-i-1]:
        if x[j-i-1]=="0":
            if c==0:
                res+="0"
                c=0
            else:
                res+="1"
                c=0
        else:
            if c==0:
                res+="0"
                c=1
            else:
                res+="1"
                c=1
    else:
        if c==0:
            res+="1"
            c=0
        else:
            res+="0"
            c=1
if c==1: res+="1"
print(res[::-1])
