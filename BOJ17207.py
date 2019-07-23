a=[];b=[];t=[];task=[0]*5;n=['Youngki','Jinwoo','Jungwoo','Junsuk','Inseo']
for _ in range(5):
    a.append([int(i) for i in input().split()])
    t.append([0]*5)
for _ in range(5):
    b.append([int(i) for i in input().split()])
for i in range(5):
    for j in range(5):
        for k in range(5):
            t[i][j]+=a[i][k]*b[k][j]
for i in range(5):
    task[i]=sum(t[i])
task=task[::-1]
print(n[task.index(min(task))])
