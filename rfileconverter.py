from rpy import *
s = r.load("data_file.Rdata")
m = r.get(s)
f = file("out.csv","wb")
f.write(str(len(m.keys())))
f.write("\n")
f.write(str(len(m.values()[0])))
f.write("\n")
for i in range(len(m.values())):
    for j in range(len(m.values()[0])):
        f.write(str(m.values()[i][j]))
        f.write("\n")
f.close()
