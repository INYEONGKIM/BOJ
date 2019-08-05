r=1
for i in range(1,int(input())+1):
    r*=i
t=str(r)[::-1];cnt=0
for x in t:
    if x=='0': cnt+=1
    else: break
print(cnt)
