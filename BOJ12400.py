dic={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l',
    'n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
n=int(input());r=""
for i in range(1,n+1):
    r+="Case #"+str(i)+": "
    s=input();l=len(s)
    for j in range(l):
        if s[j]==" ":
            r+=" "
        else:
            r+=dic[s[j]]
    r+="\n"
print(r,end="")
