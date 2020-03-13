p1_x, p1_y = map(int, __import__('sys').stdin.readline().split())
p2_x, p2_y = map(int, __import__('sys').stdin.readline().split())
p3_x, p3_y = map(int, __import__('sys').stdin.readline().split())
ccw = p1_x*p2_y + p2_x*p3_y + p3_x*p1_y - p1_y*p2_x - p2_y*p3_x - p3_y*p1_x
if ccw == 0:
    print(0)
elif ccw > 0:
    print(1)
else:
    print(-1)
