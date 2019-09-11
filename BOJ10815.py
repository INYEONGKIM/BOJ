input=__import__('sys').stdin.readline
n=int(input());a=set(int(i) for i in input().split());x=int(input());r=""
for i in input().split():
    if int(i) in a: r+='1 '
    else: r+='0 '
print(r.strip())
