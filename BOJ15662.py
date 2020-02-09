input=__import__('sys').stdin.readline

cnt = int(input())
wheels = []
rot = [0]*cnt
tops = [0]*cnt

for _ in range(cnt):
    wheels.append(input().strip())

for _ in range(int(input())):
    num, direction = map(int,input().strip().split())
    num -= 1
    rot[num] = direction # 1, -1, 0

    # right
    prev = num
    cur = num+1
    prev_dir = direction
    while cur < cnt:
        if wheels[prev][(tops[prev]+2)%8] == wheels[cur][(tops[cur]+6)%8]: break
        rot[cur] = -prev_dir
        prev_dir = -prev_dir
        prev = cur
        cur += 1

    # left
    prev = num
    cur = num-1
    prev_dir = direction
    while cur >= 0:
        if wheels[prev][(tops[prev]+6) % 8] == wheels[cur][(tops[cur]+2) % 8]: break
        rot[cur] = -prev_dir
        prev_dir = -prev_dir
        prev = cur
        cur-=1

    for i in range(cnt):
        tops[i] = (tops[i]-rot[i]) % 8
        rot[i] = 0
res=0
for i in range(cnt):
    if wheels[cnt-1-i][tops[cnt-1-i]] == '1': res += 1
print(res)
