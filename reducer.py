#!/usr/bin/env python
# source: http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

import sys;

n = 2; m = 2; l = 4;
pKey = None;
pd = 1;
output_sum = 0

for line in sys.stdin:
	(key,value) = line.strip().split("\t"); 
	arr = key.split(" ");
	(v, side) = value.split(" ");
        if pKey != None and pKey != arr:
            if arr[0] == pKey[0] and arr[1] == pKey[1]: # same output index
                output_sum += pd
                pd = 1
            else:
                output_sum += pd
                print '%s %s\t%d' % (pKey[0], pKey[1], output_sum)
                output_sum = 0
                pd = 1
	pKey = arr;
	pd *= int(v);
if pKey != None:
    output_sum += pd
    print("%s %s\t%d" % (pKey[0], pKey[1], output_sum));
