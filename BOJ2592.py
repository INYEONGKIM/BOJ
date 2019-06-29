a=[];b=[0]*100
for _ in range(10):
    a.append(int(input()))
    b[a[-1]//10]+=1
print(sum(a)//10,b.index(max(b))*10,sep='\n')
