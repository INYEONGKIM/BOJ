from collections import deque
res = ""
for _ in range(int(__import__('sys').stdin.readline())):
    cmd = str(__import__('sys').stdin.readline().strip())
    n = int(__import__('sys').stdin.readline())
    s = __import__('sys').stdin.readline().strip()[1:-1]

    if cmd.count('D') > n:
        res += 'error\n'
        continue

    if s=="":
        res += '[]\n'
        continue
    else:
        if n == 1:
            if "D" in cmd:
                res += '[]\n'
                continue
            else:
                res += f'[{s}]\n'
                continue
        else:
            l = deque(s.split(','))
            cmd = cmd.replace('RR', "")
            stat = True
            for x in cmd:
                if x == 'D':
                    if stat:
                        l.popleft()
                    else:
                        l.pop()
                else:
                    if stat: stat= False
                    else: stat = True
            if not stat:
                l.reverse()
            res += f'[{",".join(l)}]\n'
print(res, end='')
