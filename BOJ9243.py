n=int(input())
s1=input();s2=input()
l=len(s1)
res=True
if n%2==1:
    for i in range(l):
        if s1[i]==s2[i]:
            res=False
            break
else:
    for i in range(l):
        if s1[i]!=s2[i]:
            res=False
            break
if res:
    print("Deletion succeeded")
else:
    print("Deletion failed")
