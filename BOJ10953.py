n=int(input())
while n>0:
    n-=1
    l=map(int, input().split(","))
    print(sum(l))
