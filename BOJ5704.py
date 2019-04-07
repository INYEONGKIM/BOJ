res=""
while True:
    l = [False, False, False, False, False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False, False, False, False]
    s=input()
    e=len(s)
    if s=="*":
        break
    for i in range(e):
        if 'a'<=s[i]<='z':
            l[ord(s[i])-ord('a')]=True
    i=0
    while i<26:
        if not l[i]:
            res+="N\n"
            break
        i+=1
    if i==26:
        res+="Y\n"
print(res,end="")
