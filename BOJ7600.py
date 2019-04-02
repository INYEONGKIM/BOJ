while True:
    s=input().upper()
    if s=="#": break
    else:
        l=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        r = len(s)
        for i in range(r):
            if 'A'<=s[i]<='Z' and l[ord(s[i])-ord('A')]==0:
                l[ord(s[i]) - ord('A')]+=1
        res=0
        for i in range(26):
            res+=l[i]
        print(res)
