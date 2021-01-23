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

X=[]
Y=[]
R=[]
F=[]
T=[]

file='GALAXY_CAT1'
f=open(file)
lines=f.readlines()
f.close()

for i in range(0,len(lines)):
    X.append(re.split('\s+',lines[i])[0])
    Y.append(re.split('\s+',lines[i])[1])
    R.append(float(re.split('\s+',lines[i])[2])*0.99/0.9)
    F.append(re.split('\s+',lines[i])[3])
    T.append(re.split('\s+',lines[i])[4])

fout='GALAXY_CAT'
for i in range(0,len(X)):
    f=open(fout,'at')
    print(X[i],Y[i],R[i],F[i],T[i],sep=' ',file=f)
    f.close()

