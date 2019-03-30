idx=1; max=int(input())
for i in range(2, 10):
    t = int(input())
    if t>max:
        max=t; idx=i
print(max,idx,sep="\n")
