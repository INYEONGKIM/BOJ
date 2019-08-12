k,l=map(int,input().split());s=input();r="";k%=26
for i in s:
    if 'a'<=i<='z':
        r+=chr((ord(i)-ord('a')+k)%26+ord('a'))
    elif 'A'<=i<='Z':
        r+=chr((ord(i)-ord('A')+k)%26+ord('A'))
    else:
        r+=i
print(r)
