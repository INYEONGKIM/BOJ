input=__import__('sys').stdin.readline
s1=input().strip();s2=input().strip();s3=input().strip();s4=input().strip()
wheels = [s1, s2, s3, s4]
tops = [0, 0, 0, 0]
rot = [0, 0, 0, 0]

for _ in range(int(input())):
    num, direction = map(int,input().strip().split())
    num -= 1
    rot[num] = direction # 1, -1, 0

    # right
    prev = num
    cur = num+1
    prev_dir = direction
    while cur < 4:
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

    for i in range(4):
        tops[i] = (tops[i]-rot[i]) % 8
        rot[i] = 0

s = wheels[3][tops[3]]+wheels[2][tops[2]]+wheels[1][tops[1]]+wheels[0][tops[0]]
print(int(s, 2))
