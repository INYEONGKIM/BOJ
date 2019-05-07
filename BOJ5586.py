s=input()
l=len(s)
t=s[0];j=0;o=0;flag=0
for i in range(1,l+1):
    if t=='J':
        flag=1
    elif t=='I':
        if flag==2:
            j+=1
            flag=3
        elif flag==4:
            o+=1
            flag=3
        else:
            flag=3
    elif t=='O':
        if flag==1:
            flag+=1
        elif flag==3:
            flag+=1
        else:
            flag=0
    else:
        flag=0
    if i<l:
        t=s[i]
print(j,o,sep="\n")
