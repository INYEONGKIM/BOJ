n=int(input())
d = [0,1]
if n==1:
    print("0 1")
else:
    for i in range(n-1):
        d.append(d[i]+d[i+1])
    print(d[-2],d[-1])
