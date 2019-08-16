import sys
r=""
while True:
    d,m,y=map(int,sys.stdin.readline().split());f=True
    if d==0==m==y: break
    if 0<m<13:
        if m==2:
            if y%4==0 and not(y%100==0 and not (y%400==0)):
                if not 0<d<30: f=False
            else:
                if not 0<d<29: f=False
        elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            if not 0<d<32: f=False
        else:
            if not 0<d<31: f=False
    else: f=False
    if f: r+="Valid\n"
    else: r+="Invalid\n"
print(r.strip())
