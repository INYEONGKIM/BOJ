input=__import__('sys').stdin.readline;a=['Soongsil','Korea','Hanyang'];t=[int(i) for i in input().split()]
if sum(t)>=100: print('OK')
else: print(a[t.index(min(t))])
