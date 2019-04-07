res=""
n=int(input())
for k in range(1, n+1):
    le=int(input()); s=input()
    word=""
    for i in range(le):
        a = "0b"
        for j in range(8):
            if s[8*i+j]=='I': a+="1"
            else: a+="0"
        word+=chr(int(a, 2))
    res+="Case #"+str(k)+": "+word+"\n"
print(res,end="")
