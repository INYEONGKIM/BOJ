r=""
for _ in range(int(input())):
    s=input().split();t=s[1]
    if t=='+':
        if int(s[0])+int(s[2])==int(s[-1]):
            r+="correct\n"
        else:
            r+="wrong answer\n"
    elif t=='-':
        if int(s[0])-int(s[2])==int(s[-1]):
            r+="correct\n"
        else:
            r+="wrong answer\n"
    elif t=='*':
        if int(s[0])*int(s[2])==int(s[-1]):
            r+="correct\n"
        else:
            r+="wrong answer\n"
    else:
        if int(s[0])//int(s[2])==int(s[-1]):
            r+="correct\n"
        else:
            r+="wrong answer\n"
print(r,end="")
