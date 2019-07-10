n=int(input());r=""
for i in range(1,n+1):
    s=input().strip()
    if s=="5 6" or s=="6 5":
        r+="Case "+str(i)+": Sheesh Beesh\n"
    else:
        a=[int(k) for k in s.split()]
        a.sort(reverse=True)
        if a[0]==a[1]:
            if a[0]==1:
                r+="Case "+str(i)+": Habb Yakk\n"
            elif a[0]==2:
                r += "Case " + str(i) + ": Dobara\n"
            elif a[0]==3:
                r += "Case " + str(i) + ": Dousa\n"
            elif a[0]==4:
                r += "Case " + str(i) + ": Dorgy\n"
            elif a[0]==5:
                r += "Case " + str(i) + ": Dabash\n"
            else:
                r += "Case " + str(i) + ": Dosh\n"
        else:
            r += "Case " + str(i)+": "
            for k in range(2):
                if a[k]==1:
                    r+="Yakk"
                elif a[k]==2:
                    r+="Doh"
                elif a[k]==3:
                    r+="Seh"
                elif a[k]==4:
                    r+="Ghar"
                elif a[k]==5:
                    r+="Bang"
                else:
                    r+="Sheesh"
                if k==0:
                    r+=" "
                else:
                    r+="\n"
print(r,end="")
