class std:
    def __init__(self,nation,num,tot):
        self.nation = nation
        self.num = num
        self.tot = tot
n=int(input());l=[];m=[];p=0;r=""
for _ in range(n):
    a,b,c=map(int,input().split())
    l.append(std(a,b,c))
l.sort(key=lambda x:x.tot,reverse=True)
for i in range(n):
    nat=l[i].nation
    if nat not in m:
        m.append(nat);p+=1
        r+=str(nat)+" "+str(l[i].num)+"\n"
    else:
        if len(m)==1:
            m.append(nat);p+=1
            r+=str(nat)+" " + str(l[i].num)+"\n"
        else:
            if m[0]!=m[1]:
                m.append(nat);p+=1
                r+=str(nat)+" " + str(l[i].num)+"\n"
    if p==3: break
print(r,end="")
