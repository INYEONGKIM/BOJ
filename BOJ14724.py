a=["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]
n=int(input());m=-1;idx=-1
for i in range(9):
    l=[int(j) for j in input().split()]
    if max(l)>m:
        m=max(l); idx=i
print(a[idx])
