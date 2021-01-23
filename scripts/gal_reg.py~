#!/usr/local/bin/python

from __future__ import print_function
import numpy
import numpy as np
#import pyfits
#from pyslalib import slalib
#from astropy import wcs
from astropy.io import fits
import pywcs
import math
from math import *
import re
from glob import glob

name=['0108060401','0108060501','0108060601','0108060701','0108061801','0108061901','0108062101','0108062301','0555780101','0555780201','0555780301','0555780401','0555780501','0555780601','0555780701','0555780801','0555780901','0555781001','0555782301','0604960101','0604960201','0604960301','0604960401','0604960501','0604960601','0604960701','0604960801','0604960901','0604961001','0604961101','0604961201','0604961801']

for n in name:
    sky_x=[]
    sky_y=[]
    sky_r=[]
    file='/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/%s/analysis/GALAXY_CAT1' % (n)
    f=open(file)
    lines=f.readlines()
    f.close()
    for i in range(0,len(lines)):
        sky_x.append(float(re.split('\s+',lines[i])[0]))
        sky_y.append(float(re.split('\s+',lines[i])[1]))
        sky_r.append(float(re.split('\s+',lines[i])[2]))
    file = '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/%s/analysis/pnS005-cheese.fits' % (n)
    hdulist = fits.open(file)
    cra = hdulist[0].header['CRVAL1'] # cra = central ra
    cdec = hdulist[0].header['CRVAL2'] # cdec = central dec
    hdulist.close()
    
    wcs = pywcs.WCS(naxis=2)
    wcs.wcs.crpix = [25921,25921] # sky (x,y) pixel coordinate referece pixel
    wcs.wcs.cdelt = np.array([ -1.38888889e-05,   1.38888889e-05]) # pixel size 0.05"
    wcs.wcs.crval = [ float(cra) , float(cdec) ] # (ra,dec) value at reference pixel
    wcs.wcs.ctype = ['RA---TAN', 'DEC--TAN']
    num = len(sky_x)
    x = np.zeros((num))
    y = np.zeros((num))
    r = np.zeros((num))
    for i in range(0,num):
        pixcoord = np.array([[sky_x[i], sky_y[i]]])
        skycoord = wcs.wcs_pix2sky(pixcoord,1)
        radius = sky_r[i]*0.05/60.0
        x[i] = skycoord[0][0]
        y[i] = skycoord[0][1]
        r[i] = radius
    
    infile = '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/xspec/%s-galaxy.reg' % (n)
    fout = open(infile,'at')
    print('# Region file format: DS9 version 4.1',file=fout)
    print('global color=yellow dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1',file=fout)
    print('fk5',file=fout)
    fout.close()
    for i in range(0,len(x)):
        fout = open(infile,'at')
        print('+Circle(',x[i],',',y[i],',',r[i],"')",sep='',file=fout)
        fout.close()
    
