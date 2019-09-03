input=__import__('sys').stdin.readline
res=""
while True:
    s=input().strip()
    if s=="ENDOFINPUT": break
    elif s=="START" or s=="END": continue
    r=""
    for i in s:
        if 'A'<=i<='Z':
            r+=chr((ord(i)-ord('A')-5)%26+ord('A'))
        else:
            r+=i
    res+=r+'\n'
print(res.strip())
