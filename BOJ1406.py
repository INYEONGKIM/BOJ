s=list(__import__('sys').stdin.readline().strip());st=[]
for _ in range(int(__import__('sys').stdin.readline())):
    t=__import__('sys').stdin.readline().strip().split()
    if t[0]=='L':
        if s: st+=[s.pop()]
        else: continue
    elif t[0]=='D':
        if st: s+=[st.pop()]
        else: continue
    elif t[0]=='B':
        if s: s.pop()
        else: continue
    else:
        s+=[t[1]]
print(''.join(s+list(reversed(st))))
