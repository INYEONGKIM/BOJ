g=[1,2,3,3,4,10]
s=[1,2,2,2,3,5,10]
n=int(input())
for i in range(1,n+1):
    gS = 0
    sS = 0
    t = input().split(" ")
    for j in range(6):
        gS+=(g[j]*int(t[j]))
    t = input().split(" ")
    for j in range(7):
        sS+=(s[j]*int(t[j]))
    if gS==sS:
        print("Battle ",i,": No victor on this battle field",sep="")
    elif gS>sS:
        print("Battle ",i,": Good triumphs over Evil", sep="")
    else:
        print("Battle ",i,": Evil eradicates all trace of Good", sep="")
