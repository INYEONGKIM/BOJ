n=int(input());th,a=map(int,input().split());th*=a;f=False
a=[int(i) for i in input().split()];a.sort(reverse=True);r=0
for i in range(n):
    r+=a[i]
    if r>=th:
        print(i+1);f=True
        break
if not f:
    if r>=th:
        print(n)
    else:
        print("STRESS")
