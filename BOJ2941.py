s = str(__import__('sys').stdin.readline().strip()).replace("c=", 'a').replace("c-", 'a').replace("dz=", 'a').replace("d-", 'a').replace("lj", 'a').replace("nj", 'a').replace("s=", 'a').replace("z=", 'a')
print(len(s))
