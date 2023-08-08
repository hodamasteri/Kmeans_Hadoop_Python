#!/usr/bin/python
import sys

fd = open("centers.txt", 'r')
lines = fd.readlines()
fd.close()

cntDict = {}
for line in lines:    # C1\t9 3 6 11 7 13 6 10 
    line = line.strip().split('\t')  
    cluster_id = line[0]
    cluster_vals = [float(val) for val in line[1].split(' ')]
    cntDict[cluster_id] = cluster_vals
    # example: 'C1': [9.0, 3.0, 6.0, 11.0, 7.0, 13.0, 6.0, 10.0]

for line in sys.stdin:  # for every line from blocks of randomData.txt:
    line = line.strip()
    point = [float(val) for val in line.split()]
    min_distance = float("inf")
    assigned_cluster = None
    
    for c_id, c_vals in cntDict.items():
        sum = 0
        for i in range(len(point)):
            sum += (c_vals[i]-point[i])**2
        curr_dist = sum**0.5 
        if curr_dist < min_distance:
            min_distance = curr_dist
            assigned_cluster = c_id
            
    print(assigned_cluster + '\t' + str(point))
