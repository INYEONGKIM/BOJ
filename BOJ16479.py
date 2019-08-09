import decimal
k=int(input());a,b=map(int,input().split());print(decimal.Decimal(k**2-((a-b)/2)**2))
