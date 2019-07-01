n=int(input());r=""
for i in range(n,1,-1):
    r+=str(i)+" bottles of beer on the wall, "+str(i)+" bottles of beer.\nTake one down and pass it around, "
    if i==2:
        r+=str(i-1)+" bottle of beer on the wall.\n\n"
    else:
        r+=str(i-1)+" bottles of beer on the wall.\n\n"
r+="1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\n"
if n==1:
    r+="No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 1 bottle of beer on the wall."
else:
    r+="No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, "+str(n)+" bottles of beer on the wall."
print(r,end="")
