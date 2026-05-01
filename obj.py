import os
txt=".intel_syntax noprefix\n"
for a in range(1,10):
    txt=txt+"a"+str(a)+":\n.ascii  \"" +(a*"*")+"\\0\"\n"
f1=open("out.s","w")
f1.write(txt)
f1.close()
os.system("as --32 -o out.o out.s")
os.system("cat out.o")
os.system("objdump -x out.o")