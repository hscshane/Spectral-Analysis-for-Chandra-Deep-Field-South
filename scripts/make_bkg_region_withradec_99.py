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
  chandra_ra.append(float(re.split('\s+',lines[i])[0]))
  chandra_dec.append(float(re.split('\s+',lines[i])[1]))
  chandra_type.append(str(re.split('\s+',lines[i])[3]))

num = len(chandra_ra)
r = np.zeros((num))

for i in range(0,num):
  theta = math.acos(math.sin(math.radians(chandra_dec[i])) * math.sin(math.radians(cdec)) + math.cos(math.radians(chandra_dec[i])) * math.cos(math.radians(cdec)) * math.cos(math.radians((chandra_ra[i]-cra)))) 
  chandra_theta.append(math.degrees(theta))
  z = float(chandra_theta[i] / 60)
  if chandra_type[i] == 'GALAXY':
    rad = float(0.99 * 16.6 + (1.08 * z)) 
    chandra_r.append(rad)
  else:
    rad = float(0.5 * 16.6 + (1.08 * z)) 
    chandra_r.append(rad)

for i in range(0,num):
	radius = chandra_r[i]/60
	r[i] = radius


file='FinoguenovCluster_fk5.reg'
f=open(file)
lines = f.readlines()
f.close()

el_ra=[]
el_dec=[]
el_maj=[]
el_min=[]
el_ang=[]

for i in range(0,len(lines)):
    el_ra.append(float(re.split('\s+',lines[i])[0]))
    el_dec.append(float(re.split('\s+',lines[i])[1]))
    el_maj.append(float(re.split('\s+',lines[i])[2]))
    el_min.append(float(re.split('\s+',lines[i])[3]))
    el_ang.append(float(re.split('\s+',lines[i])[4]))
    
numel=len(el_ra)
elmaj = np.zeros((numel))
elmin = np.zeros((numel))
for i in range(0,numel):
    r1 = el_maj[i]/60
    r2 = el_min[i]/60
    elmaj[i] = r1
    elmin[i] = r2

data2 = np.recarray((num+numel,),dtype=(numpy.record, [('SHAPE', 'S16'), ('X', '>f4', (4,)), ('Y', '>f4', (4,)), ('R', '>f4', (4,)), ('ROTANG', '>f4', (4,)), ('COMPONENT', '>i4')]))
for i in range(0,num):
    data2[i][0] = "!CIRCLE"
    data2[i][1] = (chandra_ra[i],0,0,0)
    data2[i][2] = (chandra_dec[i],0,0,0)
    data2[i][3] = (r[i],0,0,0)
    data2[i][4] = (0.,0,0,0)
    data2[i][5] = 1

for i in range(num,num+numel):
    k=i-num
    data2[i][0] = "!ELLIPSE"
    data2[i][1] = (el_ra[k],0,0,0)
    data2[i][2] = (el_dec[k],0,0,0)
    data2[i][3] = (elmaj[k],elmin[k],0,0)
    data2[i][4] = (el_ang[k],0,0,0)
    data2[i][5] = 1 
    
file='pnS005-bkg_region-sky.fits'    
hdu = pyfits.open(file)
data = hdu[1].data


nhdu1 = pyfits.PrimaryHDU()
nhdu1.header = hdu[0].header

nhdu2 =  pyfits.BinTableHDU.from_columns(data.columns, nrows=num+numel)

nhdu2.data = data2
nhdu2.header = hdu[1].header
nhdu2.header['NAXIS2']= num+numel
hdulist = pyfits.HDUList([nhdu1,nhdu2])
hdulist.writeto("pnS005-bkg_region-radec.fits")


