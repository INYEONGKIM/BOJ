# for n in range(1,15):
#     ans=0
#     a,b,c=[False]*n, [False]*(2*n-1), [False]*(2*n-1)
#     def solve(i):
#         global ans
#         if i==n: ans+=1;return;
#         for j in range(n):
#             if not (a[j] or b[i+j] or c[i-j+n-1]):
#                 a[j]=b[i+j]=c[i-j+n-1]=True
#                 solve(i+1)
#                 a[j] = b[i + j] = c[i - j + n - 1] = False
#     solve(0)
#     print(ans, end=",")
k=[1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596];print(k[int(__import__('sys').stdin.readline())-1])
