n=int(input()); res=""
for _ in range(n):
    car=int(input())
    opt=int(input())
    for _ in range(opt):
        a,b=map(int, input().split())
        car+=a*b
    res+=str(car)+"\n"
print(res)
