#!/usr/local/bin/python

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

file = 'CDFS4MS_REVISED.fits'
f = open(file)
lines = f.readlines()
f.close()

chandra_ra =[]
chandra_dec = []
chandra_r = []
chandra_theta = []
chandra_type = []
chandra_flux = []
chandra_t = []
for i in range(1,len(lines)-1):
  chandra_ra.append(float(re.split('\s+',lines[i])[0]))
  chandra_dec.append(float(re.split('\s+',lines[i])[1]))
  chandra_flux.append(float(re.split('\s+',lines[i])[3]))
  chandra_type.append(str(re.split('\s+',lines[i])[4]))
  
num = len(chandra_ra)
r = np.zeros((num))

for i in range(0,num):
  theta = math.acos(math.sin(math.radians(chandra_dec[i])) * math.sin(math.radians(cdec)) + math.cos(math.radians(chandra_dec[i])) * math.cos(math.radians(cdec)) * math.cos(math.radians((chandra_ra[i]-cra)))) 
  chandra_theta.append(math.degrees(theta))
  z = float(chandra_theta[i] / 60)
  if chandra_type[i] == 'GALAXY':
    rad = float(0.9 * 16.6 + (1.08 * z)) 
    chandra_r.append(rad)
    chandra_t.append('!GALAXY')
  else:
    rad = float(0.5 * 16.6 + (1.08 * z)) 
    chandra_r.append(rad)
    chandra_t.append('!AGN')

for i in range(0,num):
	radius = chandra_r[i]/0.05
	r[i] = radius
	
data2 = np.recarray((num,),dtype=(numpy.record, [('TYPE', 'S16'), ('X', '>f4', (4,)), ('Y', '>f4', (4,)), ('R', '>f4', (4,)), ('FLUX', '>f4',(1,)), ('ROTANG', '>f4', (4,))]))
for i in range(0,num):
    data2[i][0] = chandra_t[i]
    data2[i][1] = (chandra_ra[i],0,0,0)
    data2[i][2] = (chandra_dec[i],0,0,0)
    data2[i][3] = (r[i],0,0,0)
    data2[i][4] = chandra_flux[i]
    data2[i][5] = (0.,0,0,0)
    
file = "pnS005-bkg_region-radec.fits"
hdu = pyfits.open(file)
data = hdu[1].data


nhdu1 = pyfits.PrimaryHDU()
nhdu1.header = hdu[0].header

nhdu2 =  pyfits.BinTableHDU.from_columns(data.columns, nrows=num)

nhdu2.data = data2
nhdu2.header = hdu[1].header
nhdu2.header['NAXIS2']= 739
hdulist = pyfits.HDUList([nhdu1,nhdu2])
hdulist.writeto("pnS005-bkg_region-radec-type.fits")

