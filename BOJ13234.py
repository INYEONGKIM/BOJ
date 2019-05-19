s=input().split()
if s[1]=='OR':
    if s[0]=='true':
        print('true')
    else:
        if s[2]=='true':
            print('true')
        else:
            print('false')
else:
    if s[0]=='false':
        print('false')
    else:
        if s[2]=='true':
            print('true')
        else:
            print('false')
