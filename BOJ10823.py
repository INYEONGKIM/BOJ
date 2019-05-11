res=""
while True:
    try:
        res+=input()
    except EOFError:
        break
l=map(int, res.split(","))
print(sum(l))
