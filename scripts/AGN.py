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

degtorad = math.pi / 180

sky_x1 = []
sky_y1 = []
R1 = []
flux1 = []
radius1 = []

sky_x2 = []
sky_y2 = []
R2 = []
flux2 = []
radius2 = []

sky_x3 = []
sky_y3 = []
R3 = []
flux3 = []
radius3 = []

sky_x4 = []
sky_y4 = []
R4 = []
flux4 = []
radius4 = []


sky_x5 = []
sky_y5 = []
R5 = []
flux5 = []
radius5 = []
star_type = []

sky_x6 = []
sky_y6 = []
R6 = []
flux6 = []
radius6 = []



file = 'pnS005-cheese.fits'
hdulist = pyfits.open(file)
cra = hdulist[0].header['CRVAL1'] # cra = central ra
cdec = hdulist[0].header['CRVAL2'] # cdec = central dec
hdulist.close()


file='pnS005-bkg_region-sky-type.fits'
hdulist = pyfits.open(file)
tbdata = hdulist[1].data
for i in range(0,739):
	if tbdata[i]['TYPE'] == 'AGN':
		tempx = tbdata[i]['X']
		tempy = tbdata[i]['Y']
		tempr = tbdata[i]['R']
		tempf = tbdata[i]['FLUX']		
		if tempf > 1.0E-14:
		  sky_x1.append(float(tempx[0]))
		  sky_y1.append(float(tempy[0]))
		  R1.append(float(tempr[0]))
		  flux1.append(float(tempf))
		  star_type.append('AGN')
		elif tempf >= 1.0E-15 and tempf < 1.0E-14:
		  sky_x2.append(float(tempx[0]))
		  sky_y2.append(float(tempy[0]))
		  R2.append(float(tempr[0]))
		  flux2.append(float(tempf))
		  star_type.append('AGN')
		elif tempf >= 2.0E-16 and tempf < 1.0E-15: 
		  sky_x3.append(float(tempx[0]))
		  sky_y3.append(float(tempy[0]))
		  R3.append(float(tempr[0]))
		  flux3.append(float(tempf))
		  star_type.append('AGN')
		elif tempf >= 1.0E-16 and tempf < 2.0E-16:
		  sky_x4.append(float(tempx[0]))
		  sky_y4.append(float(tempy[0]))
		  R4.append(float(tempr[0]))
		  flux4.append(float(tempf))
		  star_type.append('AGN')
		elif tempf >= 5.0E-17 and tempf < 1.0E-16:
		  sky_x5.append(float(tempx[0]))
		  sky_y5.append(float(tempy[0]))
		  R5.append(float(tempr[0]))
		  flux5.append(float(tempf))
		  star_type.append('AGN')
		elif tempf >= 1.0E-17 and tempf < 5.0E-17:
		  sky_x6.append(float(tempx[0]))
		  sky_y6.append(float(tempy[0]))
		  R6.append(float(tempr[0]))
		  flux6.append(float(tempf))
		  star_type.append('AGN')
	else:
		continue
hdulist.close()
		
		
a = len(sky_x1)
b = len(sky_x2)
c = len(sky_x3)
d = len(sky_x4)
e = len(sky_x5)
f = len(sky_x6)

for i in range(0,a):
	rad = float(R1[i])
	radius1.append(rad)

for i in range(0,b):
	rad = float(R2[i])
	radius2.append(rad)

for i in range(0,c):
	rad = float(R3[i])
	radius3.append(rad)

for i in range(0,d):
	rad = float(R4[i])
	radius4.append(rad)

for i in range(0,e):
	rad = float(R5[i])
	radius5.append(rad)

for i in range(0,f):
	rad = float(R6[i])
	radius6.append(rad)
	

for i in range(0,a):
	fout = open('AGN_CAT1','at')
	print(sky_x1[i],sky_y1[i],radius1[i],flux1[i],star_type[i],file=fout)
	fout.close()
	
for i in range(0,b):
	fout = open('AGN_CAT2','at')
	print(sky_x2[i],sky_y2[i],radius2[i],flux2[i],star_type[i],file=fout)
	fout.close()

for i in range(0,c):
	fout = open('AGN_CAT3','at')
	print(sky_x3[i],sky_y3[i],radius3[i],flux3[i],star_type[i],file=fout)
	fout.close()	

for i in range(0,d):
	fout = open('AGN_CAT4','at')
	print(sky_x4[i],sky_y4[i],radius4[i],flux4[i],star_type[i],file=fout)
	fout.close()
	
for i in range(0,e):
	fout = open('AGN_CAT5','at')
	print(sky_x5[i],sky_y5[i],radius5[i],flux5[i],star_type[i],file=fout)
	fout.close()
	
for i in range(0,f):
	fout = open('AGN_CAT6','at')
	print(sky_x6[i],sky_y6[i],radius6[i],flux6[i],star_type[i],file=fout)
	fout.close()
	

