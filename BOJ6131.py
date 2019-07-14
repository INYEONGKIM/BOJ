n=int(input());cnt=0
for i in range(1,501):
    for j in range(1,i+1):
        if i**2==j**2+n: cnt+=1
print(cnt)
