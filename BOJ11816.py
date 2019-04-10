s=input()
if s[0]=='0' and len(s)>1:
    if s[1]=='x':
        print(format(int(s, 16), 'd'))
    else:
        print(format(int(s, 8), 'd'))
else:
    print(s)
