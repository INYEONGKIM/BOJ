def boo(str,a,b):
    if str==">":
        return a>b
    elif str==">=":
        return a>=b
    elif str=="<":
        return a<b
    elif str=="<=":
        return a<=b
    elif str=="==":
        return a==b
    elif str=="!=":
        return a!=b
i = 0
while True:
    a,b,c = input().split()
    if b=="E": break
    else:
        i+=1
        print("Case ",i,": ",sep="",end="")
        if boo(b, int(a), int(c)):
            print("true")
        else:
            print("false")
