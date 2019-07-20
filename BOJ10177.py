r=""
for _ in range(int(input())):
    n=int(input());a=[];f=True
    for _ in range(n):
        a.append([int(i) for i in input().split()])
    th=sum(a[0])
    for i in range(1,n):
        if sum(a[i])!=th:
            f=False
            break
    if f:
        for i in range(n):
            t=0
            for j in range(n):
                t+=a[j][i]
            if t!=th:
                f=False
                break
    if f:
        ta=0;tb=0
        for i in range(n):
            ta+=a[i][i]
            tb+=a[n-i-1][n-1-i]
        if ta!=th or tb!=th:
            f=False
    if f:
        r+="Magic square of size "+str(n)+'\n'
    else:
        r+="Not a magic square\n"
print(r,end="")
