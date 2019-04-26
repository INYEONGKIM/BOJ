s=input()
a,x,c= s.partition('x')
if x=="":
    print("0")
else:
    if a=="":
        print(1)
    elif a=="-":
        print(-1)
    else:
        print(a)
