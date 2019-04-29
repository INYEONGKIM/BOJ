h,m,s = map(int, input().split())
s += (m*60 + h*3600 + int(input()))
h = s//3600
m = (s%3600)//60
s = (s%3600)%60
if h>23:
    h %= 24
print(h,m,s)
