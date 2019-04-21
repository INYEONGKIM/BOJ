listAdrian = ['A','B','C']
listBruno = ['B','A','B','C']
listGoran = ['C','C','A','A','B','B']
aCnt=0; bCnt=0; gCnt=0
l = int(input())
s=input()
for i in range(l):
    if s[i] == listAdrian[i%3]: aCnt+=1
    if s[i] == listBruno[i%4]: bCnt+=1
    if s[i] == listGoran[i%6]: gCnt+=1

m = max(aCnt, bCnt, gCnt)
res=str(m)+"\n"
if m == aCnt: res+="Adrian\n"
if m == bCnt: res+="Bruno\n"
if m == gCnt: res+="Goran\n"
print(res,end="")
