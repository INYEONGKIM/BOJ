l,n=map(int,input().split())
a=[int(i) for i in input().split()];r="";b=[]
for i in range(l-1):
    b.append(abs(a[i]-a[i+1]))
for _ in range(n):
    s=0
    x,y=map(int,input().split())
    s=sum(b[x-1:y-1])
    r+=str(s)+"\n"
print(r,end="")

# l,n=map(int,input().split())
# a=[int(i) for i in input().split()];r=""
# for _ in range(n):
#     s=0
#     x,y=map(int,input().split())
#     for i in range(x,y):
#         s+=abs(a[i]-a[i-1])
#     r+=str(s)+"\n"
# print(r,end="")
