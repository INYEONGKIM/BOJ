__import__('sys').setrecursionlimit(100000)
W,n=map(int,__import__('sys').stdin.readline().split())
weight=[0]*n;value=[0]*n
for i in range(n):
    w,v=map(int,__import__('sys').stdin.readline().split())
    weight[i]=w;value[i]=v
def knapsack(cap, n):
    if cap==0 or n==0:
        return 0
    if weight[n-1]>cap:
        return knapsack(cap, n-1)
    else:
        return max(value[n-1]+knapsack(cap-weight[n-1],n-1), knapsack(cap,n-1))
print(knapsack(W,n))
