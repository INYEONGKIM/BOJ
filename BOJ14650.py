n=int(input());ans=0
def s(x,h):
    global ans
    for i in range(3):
        if i==0 and x==0: continue
        if x==n:
            if h%3==0: ans+=1;return
        else:
            s(x+1,h+i)
s(0,0)
print(ans)
