#!/usr/bin/python
import random

fd = open("randomData.txt", 'w')
for row in range(1200000):
    for col in range(8):
        fd.write(str(random.randrange(1,20)))
        fd.write(" ")
    fd.write("\n")
fd.close()  
