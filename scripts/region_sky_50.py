#!/usr/local/bin/python

import numpy
import numpy as np
#import pyfits
#from pyslalib import slalib
from astropy import wcs
from astropy.io import fits
#import pywcs
import math
from math import *
import re
from glob import glob

degtorad = math.pi/180

file = 'pnS005-cheese.fits'
hdulist = fits.open(file)
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
for i in range(1,len(lines)-1):
  chandra_ra.append(float(re.split('\s+',lines[i])[0]))
  chandra_dec.append(float(re.split('\s+',lines[i])[1]))
  chandra_flux.append(float(re.split('\s+',lines[i])[3]))
  chandra_type.append(str(re.split('\s+',lines[i])[4]))

num = len(chandra_ra)

for i in range(0,num):
  theta = math.acos(math.sin(math.radians(chandra_dec[i])) * math.sin(math.radians(cdec)) + math.cos(math.radians(chandra_dec[i])) * math.cos(math.radians(cdec)) * math.cos(math.radians((chandra_ra[i]-cra)))) 
  chandra_theta.append(math.degrees(theta))
  z = float(chandra_theta[i] * 60)
  if chandra_type[i] == 'GALAXY':
    rad = float(0.5 * 16.6 + (1.27 * z)) 
    chandra_r.append(rad)
  else:
    rad = float(0.5 * 16.6 + (1.27 * z)) 
    chandra_r.append(rad)

wcs = wcs.WCS(naxis=2)
wcs.wcs.crpix = [25921,25921] # sky (x,y) pixel coordinate referece pixel
wcs.wcs.cdelt = np.array([ -1.38888889e-05,   1.38888889e-05]) # pixel size 0.05"
wcs.wcs.crval = [ float(cra) , float(cdec) ] # (ra,dec) value at reference pixel
wcs.wcs.ctype = ['RA---TAN', 'DEC--TAN']
num = len(chandra_ra)
x = np.zeros((num))
y = np.zeros((num))
r = np.zeros((num))
for i in range(0,num):
    skycoord = np.array([[chandra_ra[i], chandra_dec[i]]])
    pixcoord = wcs.wcs_world2pix(skycoord,1)
    radius = chandra_r[i]/0.05
    x[i] = pixcoord[0][0]
    y[i] = pixcoord[0][1]
    r[i] = radius
   # print "circle(",pixcoord[0][0],",",pixcoord[0][1],",",radius,")"


data2 = np.recarray((num,),dtype=(numpy.record, [('TYPE', 'S16'), ('X', '>f4', (4,)), ('Y', '>f4', (4,)), ('R', '>f4', (4,)), ('FLUX', '>f4',(1,)), ('ROTANG', '>f4', (4,))]))
for i in range(0,num):
  #if chandra_type[i] == 'GALAXY':
    data2[i][0] = chandra_type[i]
    data2[i][1] = (x[i],0,0,0)
    data2[i][2] = (y[i],0,0,0)
    data2[i][3] = (r[i],0,0,0)
    data2[i][4] = chandra_flux[i]
    data2[i][5] = (0.,0,0,0)


file = "pnS005-bkg_region-sky-original.fits"
hdu = fits.open(file)
data = hdu[1].data


nhdu1 = fits.PrimaryHDU()
nhdu1.header = hdu[0].header

nhdu2 =  fits.BinTableHDU.from_columns(data.columns, nrows=num)

nhdu2.data = data2
nhdu2.header = hdu[1].header
nhdu2.header['NAXIS2']= 739
hdulist = fits.HDUList([nhdu1,nhdu2])
hdulist.writeto("pnS005-bkg_region-sky-type.fits")
