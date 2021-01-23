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
star_type = []

xmm_x = []
xmm_y = []
xmm_r = []

infile='pnS005-bkg_region-sky-original.fits'
hdu = pyfits.open(infile)
data = hdu[1].data
lnum = len(data)
for i in range(0,lnum):
	tx = data[i]['X']
	ty = data[i]['Y']
	tr = data[i]['R']
	xmm_x.append(float(tx[0]))
	xmm_y.append(float(ty[0]))
	xmm_r.append(float(tr[0]))
hdu.close()	

file='pnS005-bkg_region-sky-type.fits'
hdulist = pyfits.open(file)
tbdata = hdulist[1].data
for i in range(0,739):
	if tbdata[i]['TYPE'] == 'GALAXY':
		tempx = tbdata[i]['X']
		tempy = tbdata[i]['Y']
		tempr = tbdata[i]['R']
		tempf = tbdata[i]['FLUX']
		flag = 0
		for k in range(0,lnum):
			difx = xmm_x[k]-tempx[0]
			dify = xmm_y[k]-tempy[0]
			difr = (math.sqrt(difx**(2)+dify**(2)))
			if difr <= xmm_r[k]:
			  flag = 1
			  break
		if flag == 1:
		  continue
		else:
#		  if tempf > 1.0E-17 and tempf < 2.0E-16:
		  sky_x1.append(float(tempx[0]))
		  sky_y1.append(float(tempy[0]))
		  R1.append(float(tempr[0]))
		  flux1.append(float(tempf))
		  star_type.append('GALAXY')
#		elif tempf >= 5.0E-17 and tempf < 1.0E-16:
#		  sky_x2.append(float(tempx[0]))
#		  sky_y2.append(float(tempy[0]))
#		  R2.append(float(tempr[0]))
#		  flux2.append(float(tempf))
#		  star_type.append('GALAXY')
#		elif tempf >= 1.0E-16 and tempf < 2.0E-16: 
#		  sky_x3.append(float(tempx[0]))
#		  sky_y3.append(float(tempy[0]))
#		  R3.append(float(tempr[0]))
#		  flux3.append(float(tempf))
#		  star_type.append('GALAXY')
#		  else:
#		    sky_x4.append(float(tempx[0]))
#		    sky_y4.append(float(tempy[0]))
#		    R4.append(float(tempr[0]))
#		    flux4.append(float(tempf))
#		    star_type.append('GALAXY')
	else:
		continue
hdulist.close()
		
		
a = len(sky_x1)
#b = len(sky_x2)
#c = len(sky_x3)
#d = len(sky_x4)

for i in range(0,a):
	rad = float(R1[i])
	radius1.append(rad)

#for i in range(0,b):
#	rad = float(R2[i]-132.8)
#	radius2.append(rad)

#for i in range(0,c):
#	rad = float(R3[i]-132.8)
#	radius3.append(rad)

#for i in range(0,d):
#	rad = float(R4[i])
#	radius4.append(rad)
	

for i in range(0,a):
	fout = open('GALAXY_CAT','at')
	print(sky_x1[i],sky_y1[i],radius1[i],flux1[i],star_type[i],file=fout)
	fout.close()
	
#for i in range(0,b):
#	fout = open('GALAXY_CAT2','at')
#	print(sky_x2[i],sky_y2[i],radius2[i],flux2[i],star_type[i],file=fout)
#	fout.close()

#for i in range(0,c):
#	fout = open('GALAXY_CAT3','at')
#	print(sky_x3[i],sky_y3[i],radius3[i],flux3[i],star_type[i],file=fout)
#	fout.close()	

#for i in range(0,d):
#	fout = open('GALAXY_CAT','at')
#	print(sky_x4[i],sky_y4[i],radius4[i],flux4[i],star_type[i],file=fout)
#	fout.close()
	

