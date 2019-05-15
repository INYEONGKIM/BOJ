a,b=map(int,input().split())
stat="Accepted"
for _ in range(a):
    s=input().split()
    if s[0]!=s[1]:
        stat="Wrong Answer"
        break
if stat=="Accepted":
    for _ in range(b):
        s=input().split()
        if s[0]!=s[1]:
            stat="Why Wrong!!!"
            break
print(stat)
