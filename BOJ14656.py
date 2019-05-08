n=int(input())
s=[int(i) for i in input().split()]
cnt=0
for i in range(n):
    if i+1!=s[i]: cnt+=1
print(cnt)
