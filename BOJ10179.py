r=""
for _ in range(int(input())):
    r+='$'+format(float(input())*0.8,".2f")+'\n'
print(r,end="")
