n=int(input());r=""
while True:
    i=int(input())
    if i==0: break
    if i%n==0: r+=str(i)+" is a multiple of "
    else: r+=str(i)+" is NOT a multiple of "
    r+=str(n)+".\n"
print(r,end="")
