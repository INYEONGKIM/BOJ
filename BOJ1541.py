s=input().split("-")
if s[0]=="":
    res=0
else:
    res=sum(map(int,s[0].split("+")))
for i in range(1,len(s)):
    res-=sum(map(int,s[i].split("+")))
print(res)
