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

X =[]
Y = []
R = []

file = 'pnS005-cheese.fits'
hdulist = pyfits.open(file)
cra = hdulist[0].header['CRVAL1'] # cra = central ra
cdec = hdulist[0].header['CRVAL2'] # cdec = central dec
hdulist.close()


for i in range(0,138):
    file = "%d""-galaxy.txt" % (i)
    f = open(file)
    lines = f.readlines()
    f.close()
    X.append(float(re.split('\s+',lines[0])[0]))
    Y.append(float(re.split('\s+',lines[0])[1]))
    R.append(float(re.split('\s+',lines[0])[2]))
    
wcs = pywcs.WCS(naxis=2)
wcs.wcs.crpix = [25921,25921] # sky (x,y) pixel coordinate referece pixel
wcs.wcs.cdelt = np.array([ -1.38888889e-05,   1.38888889e-05]) # pixel size 0.05"
wcs.wcs.crval = [ float(cra) , float(cdec) ] # (ra,dec) value at reference pixel
wcs.wcs.ctype = ['RA---TAN', 'DEC--TAN']
num = len(X)
RA = np.zeros((num))
DEC= np.zeros((num))
radius = np.zeros((num))
for i in range(0,num):
    pixcoord = np.array([[X[i], Y[i]]])
    skycoord = wcs.wcs_pix2sky(pixcoord,1)
    rad = R[i]*0.05/60.
    RA[i] = skycoord[0][0]
    DEC[i] = skycoord[0][1]
    radius[i] = rad

file = 'galaxy.reg'
f = open(file,'at')
print('# Region file format: DS9 version 4.1',file=f)
print('global color=yellow dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1',file=f)
print('fk5',file=f) 
f.close()
  
for i in range(0,num):
    file = 'galaxy.reg'
    f = open(file,'at')
    print('Circle(',RA[i],',',DEC[i],',',radius[i],"')",sep='',file=f)
    f.close()


