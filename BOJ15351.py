import sys
r=""
for _ in range(int(sys.stdin.readline())):
    s=sys.stdin.readline().strip();t=0
    for i in s:
        if i!=' ':
            t+=ord(i)-ord('A')+1
    if t==100:
        r+='PERFECT LIFE\n'
    else:
        r+=str(t)+'\n'
print(r,end="")
