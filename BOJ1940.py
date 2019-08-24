input=__import__('sys').stdin.readline
n=int(input());t=int(input());a=[int(i) for i in input().split()];c=0;s=set()
for i in range(n):
    if t>a[i]:
        if t-a[i] in s:
            c+=1
        else:
            s.add(a[i])
print(c)
