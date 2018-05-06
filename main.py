import json
import os
with open('data1.json','r') as f:
    with open("newfile.json",'w')as f2:
        firstline="["+f.readline()+","
        f2.write(firstline)
        for line in f:
            f2.write(line+",")
        f2.seek(-1, os.SEEK_END)
        f2.truncate()
        f2.write("]")















