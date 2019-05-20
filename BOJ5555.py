r=input(); n=int(input()); cnt=0
for _ in range(n):
    s=input()
    s+=s
    if r in s:
        cnt+=1
print(cnt)
