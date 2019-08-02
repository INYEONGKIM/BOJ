a=[int(i) for i in input().split()];b=[int(i) for i in input().split()]
at=0;bt=0;f=False
for i in range(9):
    at+=a[i]
    if at>bt: f=True
    bt+=b[i]
    if at>bt: f=True
print((f and sum(a)<sum(b)) and "Yes" or "No")
