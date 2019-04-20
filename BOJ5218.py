n=int(input())
r=""
for i in range(1,n+1):
    s1,s2=map(str, input().split())
    x=len(s1)
    res=""
    for j in range(x):
        if ord(s2[j]) >= ord(s1[j]):
            res+=" "+str(ord(s2[j]) - ord(s1[j]))
        else:
            res += " " + str(ord(s2[j]) + 26 - ord(s1[j]))
    r+="Distances:"+res+"\n"
print(r,end="")
