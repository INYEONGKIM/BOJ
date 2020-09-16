alp = "abcdefghijklmnopqrstuvwxyz"
res = ""
while True:
    s = __import__('sys').stdin.readline().strip()
    if s == "#":
        break
    x, y, z = s.split()
    t = ""
    for i in range(len(x)):
        dif = (ord(y[i]) - ord(x[i]) + 26) % 26
        t += alp[(ord(z[i]) - ord('a') + dif) % 26]
    res += s + " " + t + "\n"
print(res, end="")
