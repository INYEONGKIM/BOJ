input=__import__('sys').stdin.readline
r=""
while True:
    n=int(input())
    if n==0: break
    for i in range(n):
        r+='*'*(i+1)+'\n'
print(r,end="")
