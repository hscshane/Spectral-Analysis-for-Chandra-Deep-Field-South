#!/usr/bin/python

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

file = 'chandra_cdfs.fits'
f = open(file)
lines = f.readlines()
f.close()

chandra_ra =[]
chandra_dec = []
chandra_r = []
for i in range(1,len(lines)-1):
  chandra_ra.append(float(re.split('\s+',lines[i])[2]))
  chandra_dec.append(float(re.split('\s+',lines[i])[3]))
  chandra_r.append(8.0)


wcs = pywcs.WCS(naxis=2)
wcs.wcs.crpix = [25921,25921] # sky (x,y) pixel coordinate referece pixel
wcs.wcs.cdelt = np.array([ -1.38888889e-05,   1.38888889e-05]) # pixel size 0.05"
wcs.wcs.crval = [ 5.30917083333333E+01 , -2.77980833333333E+01 ] # (ra,dec) value at reference pixel
wcs.wcs.ctype = ['RA---TAN', 'DEC--TAN']
num = len(chandra_ra)
x = np.zeros((num))
y = np.zeros((num))
r = np.zeros((num))
for i in range(0,num):
    skycoord = np.array([[chandra_ra[i], chandra_dec[i]]])
    pixcoord = wcs.wcs_sky2pix(skycoord,1)
    radius = chandra_r[i]/0.05
    x[i] = pixcoord[0][0]
    y[i] = pixcoord[0][1]
    r[i] = radius
    print "circle(",pixcoord[0][0],",",pixcoord[0][1],",",radius,")"


data2 = np.recarray((num,),dtype=(numpy.record, [('SHAPE', 'S16'), ('X', '>f4', (4,)), ('Y', '>f4', (4,)), ('R', '>f4', (4,)), ('ROTANG', '>f4', (4,)), ('COMPONENT', '>i4')]))
for i in range(0,num):
    data2[i][0] = "!CIRCLE"
    data2[i][1] = (x[i],0,0,0)
    data2[i][2] = (y[i],0,0,0)
    data2[i][3] = (r[i],0,0,0)
    data2[i][4] = (0.,0,0,0)
    data2[i][5] = 1


file = "pnS005-bkg_region-sky.fits"
hdu = pyfits.open(file)
data = hdu[1].data


nhdu1 = pyfits.PrimaryHDU()
nhdu1.header = hdu[0].header

nhdu2 =  pyfits.BinTableHDU.from_columns(data.columns, nrows=num)

nhdu2.data = data2
nhdu2.header = hdu[1].header
nhdu2.header['NAXIS2']= 739
hdulist = pyfits.HDUList([nhdu1,nhdu2])
hdulist.writeto("cdfs-bkg_region-sky.fits")

