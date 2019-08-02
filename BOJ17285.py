s=input();k=int(ord(s[0]))^int(ord('C'));r=""
for i in s:
    r+=chr(int(ord(i))^k)
print(r)
