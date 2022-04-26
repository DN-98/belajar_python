f = open("avocado.csv")
o = f.readlines()
f2 = open("avocado_baru.txt",'w')
# print(o)
for i in o:
    f2.writelines(f"({i})")
