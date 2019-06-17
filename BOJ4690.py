for a in range(6,101):
    for b in range(2,a):
        for c in range(b+1,a):
            for d in range(c+1,a):
                if a**3 == b**3+c**3+d**3:
                    print("Cube = ",a,", Triple = (",b,",",c,",",d,")",sep="")
