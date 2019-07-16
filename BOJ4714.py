r=""
while True:
    x=float(input())
    if x<0:
        break
    r+="Objects weighing "+format(x,".2f")+" on Earth will weigh "+format(x*0.167,".2f")+" on the moon.\n"
print(r,end="")
