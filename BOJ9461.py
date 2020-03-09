res=""
p=[1]*100
p[3]=2;p[4]=2;p[5]=3;p[6]=4;p[7]=5;p[8]=7;p[9]=9
for i in range(10, 100):
    p[i] = p[i-1] + p[i-5]
for _ in range(int(__import__('sys').stdin.readline())):
    res += f'{p[int(__import__("sys").stdin.readline())-1]}\n'
print(res.strip())
