n=int(input())-2
if n==-1:
    print(1)
else:
    if (n//4)%2==0:
        print(n%4+2)
    else:
        print(5-n%4-1)
