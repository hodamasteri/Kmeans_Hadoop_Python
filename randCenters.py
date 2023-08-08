#!/usr/bin/python
import random

fd = open("randomData.txt", "r")
lines = fd.readlines()
fd.close()

fd = open("centers.txt", 'w') # Initial Centers        
for i in range(1,13):
    fd.write("C"+str(i)+"\t"+str(random.choice(lines)))
fd.close()
