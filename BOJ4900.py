d = {
    '0':'063', '063':'0',
    '1':'010', '010':'1',
    '2':'093', '093':'2',
    '3':'079', '079':'3',
    '4':'106', '106':'4',
    '5':'103', '103':'5',
    '6':'119', '119':'6',
    '7':'011', '011':'7',
    '8':'127', '127':'8',
    '9':'107', '107':'9'
}
res = ""
while True:
    s = __import__('sys').stdin.readline().strip()
    if s == 'BYE':
        break
    res += s
    a, b = s[:-1].split('+')
    al = len(a)
    bl = len(b)
    a_num = ""
    b_num = ""
    for i in range(0, al-2, 3):
        a_num += d[a[i:i+3]]
    for i in range(0, bl-2, 3):
        b_num += d[b[i:i+3]]
    r = str(int(a_num) + int(b_num))
    for x in r:
        res += d[x]
    res += '\n'

print(res, end="")
