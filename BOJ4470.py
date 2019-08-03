import sys
r=""
for i in range(1,1+int(sys.stdin.readline())):
    r+=str(i)+'. '+sys.stdin.readline()
print(r,end="")
