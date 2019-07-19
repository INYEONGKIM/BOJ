n=int(input());a=[int(i) for i in input().split()];f=0;cnt=0
for i in range(n):
    if a[i]==f:
        cnt+=1
        f=(f+1)%3
print(cnt)
