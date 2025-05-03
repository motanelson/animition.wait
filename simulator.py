
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
for z in ranges(3):
    for y in ranges(3):
        for x in ranges(3):
             print (str(z)+","+str(y)+","+str(x))