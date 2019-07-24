r=""
for _ in range(int(input())):
    s=input();tn=s[-2]+s[-1]
    if tn=='ne':
        r+=s[:-2]+'anes\n'
    else:
        t=s[-1]
        if t=='a' or t=='o' or t=='u':
            r+=s+'s\n'
        elif t=='i' or t=='y':
            r+=s[:-1]+'ios\n'
        elif t=='l' or t=='r' or t=='v':
            r+=s+'es\n'
        elif t=='n':
            r+=s[:-1]+'anes\n'
        elif t=='t' or t=='w':
            r+=s+'as\n'
        else:
            r+=s+'us\n'
print(r,end="")
