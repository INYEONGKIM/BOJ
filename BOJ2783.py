l=[]
a,b=map(int, input().split(" "))
l.append(1000*a/b)
n = int(input())
for i in range(n):
    a, b = map(int, input().split(" "))
    l.append(1000 * a / b)
print("%.2f" %min(l))
