a,b,n=map(int,input().split());r=""
for i in range(1,n+1):
    if i%a==0 and i%b==0:
        r+="FizzBuzz\n"
    elif i%a==0:
        r+="Fizz\n"
    elif i%b==0:
        r+="Buzz\n"
    else:
        r+=str(i)+"\n"
print(r,end="")
