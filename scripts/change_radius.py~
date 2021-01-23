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

file = 'pnS005-cheese.fits'
hdulist = pyfits.open(file)
cra = hdulist[0].header['CRVAL1'] # cra = central ra
cdec = hdulist[0].header['CRVAL2'] # cdec = central dec
hdulist.close()

file='CDFS4MS.fits'
f = open(file)
lines = f.readlines()
f.close()

chandra_ra =[]
chandra_dec = []
chandra_r = []
chandra_theta = []
chandra_type = []
for i in range(1,len(lines)-1):
  chandra_ra.append(float(re.split('\s+',lines[i])[1]))
  chandra_type.append(str(re.split('\s+',lines[i])[3]))
  chandra_dec.append(float(re.split('\s+',lines[i])[2]))
  #chandra_r.append(160)
  
num = len(chandra_ra)
print(repr(num))
r = np.zeros((num))

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

for i in range(0,num):
	radius = chandra_r[i]/0.05
	r[i] = radius

file = "pnS005-bkg_region-det.fits"
hdu = pyfits.open(file,mode='update')
tbdata = hdu[1].data

for i in range(0,num):
    tbdata[i]['R'] = [    r[i],       0.,       0.,       0.]
    	
hdu.flush()
    

