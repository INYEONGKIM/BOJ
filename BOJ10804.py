a=[int(i+1) for i in range(20)]
for _ in range(10):
    l,r=map(int,input().split())
    x=a[:l-1];y=a[l-1:r];y=y[::-1];z=a[r:]
    a=x+y+z
print(' '.join(map(str,a)))
