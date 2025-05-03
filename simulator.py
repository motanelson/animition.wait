
def ranges(n):
    t=True
    rets=[]
    nn=0
    while t:
        rets=rets+[nn]
        nn=nn+1
        if nn==n or nn>n:
            t=False
    return rets
print ("\033c\033[43;30m\nenter simulator\n")
x=0
y=0
z=0
w=0
s=list(ranges(3))
for w in s:
    for z in s:
        for y in s:
            for x in s:
                print (str(w)+","+str(z)+","+str(y)+","+str(x))