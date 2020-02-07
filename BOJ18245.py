c=2;r=''
while True:
    s=__import__('sys').stdin.readline().strip()
    if s=='Was it a cat I saw?': break
    l=len(s)
    for i in range(0, l, c):
        r+=s[i]
    c+=1;r+='\n'
print(r, end='')
