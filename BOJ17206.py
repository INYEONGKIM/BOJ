n=int(input());a=[int(i) for i in input().split()];r=""
for i in range(n):
    d3=a[i]//3;d7=a[i]//7;d21=a[i]//21
    r+=str(3*(d3*(d3+1)//2)+7*(d7*(d7+1)//2)-21*(d21*(d21+1)//2))+'\n'
print(r,end="")
