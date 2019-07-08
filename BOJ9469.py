n=int(input());r=""
for _ in range(1,n+1):
    s=input().split()
    r+=s[0]+" "+str(float(s[1])/(float(s[2])+float(s[3]))*float(s[4]))+'\n'
print(r,end="")
