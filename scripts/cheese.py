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

file = '0108060401-pnS005-cheese.fits'
hdulist = pyfits.open(file)
cra = hdulist[0].header['CRVAL1'] # cra = central ra
cdec = hdulist[0].header['CRVAL2'] # cdec = central dec
hdulist.close()

file = 'CDFS4MS.fits'
f = open(file)
lines = f.readlines()
f.close()

chandra_ra =[]
chandra_dec = []
chandra_r = []
chandra_theta = []
chandra_type = []
for i in range(1,len(lines)-1):
  chandra_ra.append(float(re.split('\s+',lines[i])[0]))
  chandra_dec.append(float(re.split('\s+',lines[i])[1]))
  chandra_type.append(str(re.split('\s+',lines[i])[3]))

num = len(chandra_ra)

for i in range(0,num):
  theta = math.acos(math.sin(math.radians(chandra_dec[i])) * math.sin(math.radians(cdec)) + math.cos(math.radians(chandra_dec[i])) * math.cos(math.radians(cdec)) * math.cos(math.radians((chandra_ra[i]-cra)))) 
  chandra_theta.append(math.degrees(theta))
  z = float(chandra_theta[i] / 60)
  if chandra_type[i] == 'GALAXY':
    rad = float(0.9 * 16.6 + (1.08 * z)) 
    chandra_r.append(rad)
  else:
    rad = float(0.5 * 16.6 + (1.08 * z)) 
    chandra_r.append(rad)

wcs = pywcs.WCS(naxis=2)
wcs.wcs.crpix = [450.91,450.91] # sky (x,y) pixel coordinate referece pixel
wcs.wcs.cdelt = np.array([ -6.94444444e-04,   6.94444444e-04]) # pixel size 2.5"
wcs.wcs.crval = [ float(cra) , float(cdec) ] # (ra,dec) value at reference pixel
wcs.wcs.ctype = ['RA---TAN', 'DEC--TAN']
num = len(chandra_ra)
x = np.zeros((num))
y = np.zeros((num))
r = np.zeros((num))
for i in range(0,num):
    skycoord = np.array([[chandra_ra[i], chandra_dec[i]]])
    pixcoord = wcs.wcs_sky2pix(skycoord,1)
    radius = chandra_r[i]/2.5
    x[i] = pixcoord[0][0]
    y[i] = pixcoord[0][1]
    r[i] = radius
   # print "circle(",pixcoord[0][0],",",pixcoord[0][1],",",radius,")"

f = open("cdfs.reg", "at")
print("+Circle(455.9,391.1,347.1761)",file = f)
for i in range(0,num):
    f = open("cdfs.reg", "at")
    print("-Circle(",x[i],",",y[i],",",r[i],")",sep='',file = f)

