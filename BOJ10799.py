s = str(__import__('sys').stdin.readline().strip()).replace("()","0")
res = 0
sticker = 0
for x in s:
    if x == "(":
        sticker += 1
    elif x == "0":
        res += sticker
    else:
        sticker -= 1
        res += 1
print(res)
