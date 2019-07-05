import hashlib
s=input()
h=hashlib.new('ripemd160')
h.update(s.encode('utf-8'))
print(h.hexdigest())
