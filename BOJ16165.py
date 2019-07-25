import sys
input=sys.stdin.readline
g,q=map(int,input().split());gl=[];gidx=[]
for _ in range(g):
    gidx.append(input());t=[]
    for i in range(int(input())):
        t.append(input())
    t.sort()
    gl.append(t)
r=""
for _ in range(q):
    quiz=input();f=input()
    if f=='1\n':
        for i in range(g):
            for j in gl[i]:
                if j==quiz:
                    r+=gidx[i]
    else:
        i=gidx.index(quiz)
        for j in gl[i]:
            r+=j
print(r,end="")
