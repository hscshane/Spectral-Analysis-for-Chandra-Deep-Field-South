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

degtorad = math.pi/180

file='poly_output.reg'
f=open(file)
lines=f.readlines()
f.close()

chandra_ra=[]
chandra_dec=[]

for i in range(0,len(lines)):
    chandra_ra.append(float(re.split('\s+',lines[i])[2]))
    chandra_dec.append(float(re.split('\s+',lines[i])[3]))
   
num=len(chandra_ra)

f=open('chandra.reg','at')
print('&&((DETX,DETY) IN polygon(',end='',file=f)

for i in range(0,num-1):
    f=open('chandra.reg','at')
    print(chandra_ra[i],chandra_dec[i],sep=',',end=',',file=f)
    
f=open('chandra.reg','at')
print(chandra_ra[num-1],',',chandra_dec[num-1],'))',sep='',end='',file=f)



