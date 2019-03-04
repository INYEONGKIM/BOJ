import base64

s1 = input()
b1 = s1.encode("UTF-8")
d = base64.b32decode(b1)
s2 = d.decode("UTF-8")
print(s2)
