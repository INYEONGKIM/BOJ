h,m=map(int,input().split());m+=60*h-45
if m<0:
    m+=24*60
print(m//60,m%60)
