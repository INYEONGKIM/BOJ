n=int(input());a=set(int(i) for i in input().split());x=int(input());b=[int(i) for i in input().split()];r=""
for i in range(x):
    if b[i] in a:
        r+="1\n"
    else:
        r+="0\n"
print(r,end="")
