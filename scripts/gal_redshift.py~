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

file = 'pnS005-cheese.fits'
hdulist = fits.open(file)
cra = hdulist[0].header['CRVAL1'] # cra = central ra
cdec = hdulist[0].header['CRVAL2'] # cdec = central dec
hdulist.close()

ra =[]
dec = []
r = []
theta = []
redshift = []
flux = []

file='galaxy_cat.fits'
hdu = fits.open(file)
data = hdu[1].data

for i in range(0,len(data)):
    ra.append(data[i]['RA'])
    dec.append(data[i]['DEC'])
    redshift.append(data[i]['REDSHIFT'])
    flux.append(data[i]['FB_FLUX'])
    
wcs = wcs.WCS(naxis=2)
wcs.wcs.crpix = [25921,25921] # sky (x,y) pixel coordinate referece pixel
wcs.wcs.cdelt = np.array([ -1.38888889e-05,   1.38888889e-05]) # pixel size 0.05"
wcs.wcs.crval = [ float(cra) , float(cdec) ] # (ra,dec) value at reference pixel
wcs.wcs.ctype = ['RA---TAN', 'DEC--TAN']
num = len(ra)
x = np.zeros((num))
y = np.zeros((num))
r = np.zeros((num))
for i in range(0,num):
    skycoord = np.array([[ra[i], dec[i]]])
    pixcoord = wcs.wcs_world2pix(skycoord,1)
    x[i] = pixcoord[0][0]
    y[i] = pixcoord[0][1]
    
for i in range(0,num):
	fout = open('gal_redshift.txt','at')
	print(x[i],y[i],redshift[i],flux[i],file=fout)
	fout.close()

