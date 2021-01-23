#!/usr/local/bin/python

from __future__ import print_function
import numpy
import numpy as np
import pyfits
from pyslalib import slalib
import pywcs
import math
from math import *
import re
from glob import glob

exposure = []
backscal = []

for i in range(0,152):
         file = "%d""galaxy.pi" % (i)
         fout = open("exposure.lis",'at')
         fback = open("backscal.lis",'at')
         hdulist = pyfits.open(file)
         keys = hdulist[1].header.keys()
         if 'EXPOSURE' in keys:
             x = hdulist[1].header['EXPOSURE']
             print(x,file=fout)
             exposure.append(x)
         else:
            continue
         if 'BACKSCAL' in keys:
            y = hdulist[1].header['BACKSCAL']
            print(y,file=fback)
            backscal.append(float(y))
         else:
	    continue
	   
	   
numx = sum(exposure)/float(len(exposure))
numy = float(sum(backscal))

print('count: ',len(exposure),file=fout)
print('average: ',numx,file=fout)
print('count: ',len(backscal),file=fback)
print('average: ',numy,file=fback)  

del exposure[:]
del backscal[:]
