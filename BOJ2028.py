n=int(input());r=""
for i in range(n):
    x=int(input());xl=len(str(x))
    y=str(x**2);yl=len(y)
    if y[yl-xl:]==str(x):
        r+="YES\n"
    else:
        r+="NO\n"
print(r,end="")
