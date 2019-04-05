res=""
while True:
    s = input()
    if s=="EOI":
        break;
    else:
        s=s.upper()
        if s.find("NEMO")==-1:
            res+="Missing\n"
        else:
            res+="Found\n"
print(res)
