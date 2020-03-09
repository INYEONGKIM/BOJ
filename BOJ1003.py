res = ""
d0=[0]*41
d1=[0]*41
d0[0]=1;d0[2]=1
d1[1]=1;d1[2]=1
for i in range(3, 41):
    d0[i]=d0[i-1]+d0[i-2]
    d1[i]=d1[i-1]+d1[i-2]
for _ in range(int(__import__('sys').stdin.readline())):
    n=int(__import__('sys').stdin.readline())
    res+=f'{d0[n]} {d1[n]}\n'
print(res, end="")
