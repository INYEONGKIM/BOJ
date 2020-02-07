s=__import__('sys').stdin.readline().strip()
if s=='0':
    print('W')
elif 'x' in s:
    a,b=s.split('x')
    _a,_b=int(a)//2,b
    if _a==-1: _a='-'
    elif _a==1: _a=''
    if b=='' or b=='+0' or b=='-0': _b=''
    else:
        if b=='+1': _b='+x'
        elif b=='-1': _b='-x'
        else: _b=b+'x'
    print(f'{_a}xx{_b}+W')
else:
    if s=='1':
        print('x+W')
    elif s=='-1':
        print('-x+W')
    else:
        print(f'{s}x+W')
