class student:
    def __init__(self, name, d, m, y):
        self.name = name
        self.d = d
        self.m = m
        self.y = y
a=[]
n=int(input())
for _ in range(n):
    t = input().split()
    e = student(t[0],int(t[1]),int(t[2]),int(t[3]))
    a.append(e)
a.sort(key=lambda x:(x.y, x.m, x.d))
print(a[-1].name, a[0].name,sep="\n")
