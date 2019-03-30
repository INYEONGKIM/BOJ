l=input()
n=int(l)
gu=9
res=0
for i in range(1,len(l)):
    res += gu*i
    gu *= 10
res += (n-int(pow(10,len(l)-1))+1)*len(l)
print(res)
