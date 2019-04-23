m=int(input()); d=int(input())
if m>2:
    res="After"
elif m<2:
    res="Before"
else:
    if d==18:
        res="Special"
    elif d<18:
        res="Before"
    else:
        res="After"
print(res)
