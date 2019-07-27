x=input();y=input();l=len(x);a="";b="";c="";d="";e=""
for i in range(l):
    if x[i]=='1':
        if y[i]=='0':
            a+='0'
            b+='1'
            c+='1'
            e+='1'
        else:
            a+='1'
            b+='1'
            c+='0'
            e+='0'
        d+='0'
    else:
        d+='1'
        if y[i]=='0':
            a+='0'
            b+='0'
            c+='0'
            e+='1'
        else:
            a+='0'
            b+='1'
            c+='1'
            e+='0'
print(a,b,c,d,e,sep="\n")
