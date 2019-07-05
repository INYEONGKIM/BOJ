a=[['A','C','A','G'],['C','G','T','A'],['A','T','C','G'],['G','A','G','T']]
n=int(input());s=input();x=-1;y=-1
for _ in range(n-1):
    t=s[-1]
    if t=='A':
        x=0
    elif t=='G':
        x=1
    elif t=='C':
        x=2
    else:
        x=3
    t=s[-2]
    if t=='A':
        y=0
    elif t=='G':
        y=1
    elif t=='C':
        y=2
    else:
        y=3
    s=s[:-2]
    s+=a[x][y]
print(s)
