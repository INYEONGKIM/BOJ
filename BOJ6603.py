import sys
from itertools import combinations
input=sys.stdin.readline
r=""
while True:
    a=[int(i) for i in input().split()]
    if a[0]==0: break
    a=a[1:];l=list(combinations(a,6))
    for i in l:
        r+=' '.join(map(str,i))+'\n'
    r+='\n'
print(r.strip())
