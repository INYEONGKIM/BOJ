s=input()
len=len(s)
res=0
for i in range(len):
    t = s[i]
    if t=='A' or t=='B' or t=='C':
        res += 3
    elif t=='D' or t=='E' or t=='F':
        res += 4
    elif t == 'G' or t == 'H' or t == 'I':
        res += 5
    elif t == 'J' or t == 'K' or t == 'L':
        res += 6
    elif t == 'M' or t == 'N' or t == 'O':
        res += 7
    elif t == 'P' or t == 'Q' or t == 'R' or t == 'S':
        res += 8
    elif t == 'T' or t == 'U' or t == 'V':
        res += 9
    else:
        res += 10
print(res)
