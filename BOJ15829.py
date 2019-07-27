n=int(input());s=input();r=0;l=len(s)
for i in range(l):
    r+=(ord(s[i])-ord('a')+1)*31**i
print(r%1234567891)
