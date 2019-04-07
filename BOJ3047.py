l=[int(i) for i in input().split()]
l.sort()
s=input()
for i in range(3):
    print(l[ord(s[i])-ord('A')],end=" ")
