#!/usr/bin/python
import sys

curr_cid = None
count = 0   # counts the number of points in a cluster
curr_centroid = []

for line in sys.stdin: # example: "C1\t[1.0,2.0,1.0,3.0,1.0,3.0,1.0,1.0]"
    line = line.strip()
    line = line.split('\t')
    cid = line[0]          # example: "C1"
    point = eval(line[1])  # example: [1.0,2.0,1.0,3.0,1.0,3.0,1.0,1.0]

    if curr_cid == cid:
        count+=1
        curr_centroid = [a + b for a, b in zip(point, curr_centroid)]
    else:
        if curr_cid:
            curr_centroid = [round(x/float(count),6) for x in curr_centroid]
            print(curr_cid + '\t' + ' '.join(str(x) for x in curr_centroid))

        curr_cid = cid
        curr_centroid = point
        count = 1

# output the last key
if curr_cid:
    curr_centroid = [round(x/float(count),6) for x in curr_centroid]
    print(curr_cid + '\t' + ' '.join(str(x) for x in curr_centroid))
