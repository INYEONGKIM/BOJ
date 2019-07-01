s=input();f=True;l=len(s)
if l>2:
    d = int(s[1])-int(s[0])
    for i in range(2,l):
        if int(s[i]) != int(s[i-1])+d:
            f=False
            break
if f:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")
