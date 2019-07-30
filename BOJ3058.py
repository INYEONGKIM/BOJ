r=""
for _ in range(int(input())):
    a=[int(i) for i in input().split()];m=101;s=0
    for i in a:
        if i%2==0:
            s+=i
            if m>i: m=i
    r+=str(s)+' '+str(m)+'\n'
print(r,end="")
