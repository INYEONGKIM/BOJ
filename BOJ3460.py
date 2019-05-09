n=int(input())
for _ in range(n):
    s=int(input())
    idx = 0
    while s!= 0:
        if s&1:
            print(idx, end=" ")
        idx+=1
        s>>=1
