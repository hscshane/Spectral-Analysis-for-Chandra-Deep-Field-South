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

x=[]
y=[]
r=[]
t=[]
ex=[]
ey=[]
emaj=[]
emin=[]
et=[]
eang=[]

file = 'pnS005-cheese.fits'
hdulist = pyfits.open(file)
cra = hdulist[0].header['CRVAL1'] # cra = central ra
cdec = hdulist[0].header['CRVAL2'] # cdec = central dec
hdulist.close()

file = 'pnS005-bkg_region-radec.fits'
hdu=pyfits.open(file)
num=len(hdu[1].data)
for i in range(0,num):
    if hdu[1].data[i][0] == '!CIRCLE':
        x.append(hdu[1].data[i][1][0])
        y.append(hdu[1].data[i][2][0])
        t.append(hdu[1].data[i][0])
        r.append(hdu[1].data[i][3][0])   
    elif hdu[1].data[i][0] == '!ELLIPSE':
        ex.append(hdu[1].data[i][1][0])
        ey.append(hdu[1].data[i][2][0])
        et.append(hdu[1].data[i][0])
        emaj.append(hdu[1].data[i][3][0])
        emin.append(hdu[1].data[i][3][1])
        eang.append(hdu[1].data[i][4][0])
    else:
        print('something is wrong')
hdu.close()
        
outf='fov.reg'
f = open(outf,'at')
print('# Region file format: DS9 version 4.1',file=f)
print('global color=yellow dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1',file=f)
print('fk5',file=f)
print('+Polygon(53.110818,-27.977576,53.094169,-27.975036,53.08179,-27.973617,53.071889,-27.965693,53.054567,-27.951361,53.03601,-27.938859,53.026029,-27.931629,53.016222,-27.923541,53.005092,-27.917195,52.992836,-27.910832,52.981598,-27.904609,52.970472,-27.898153,52.960585,-27.890782,52.950457,-27.883455,52.940113,-27.87579,52.932324,-27.867033,52.924156,-27.857182,52.925787,-27.842971,52.927582,-27.827667,52.931777,-27.815646,52.933834,-27.802529,52.936782,-27.789412,52.943442,-27.778014,52.948403,-27.76629,52.955055,-27.754448,52.961716,-27.742428,52.969022,-27.731503,52.976488,-27.720577,52.984624,-27.710745,52.993853,-27.700913,53.002844,-27.691457,53.010262,-27.681248,53.016621,-27.673597,53.025343,-27.663763,53.033738,-27.65681,53.043618,-27.648719,53.058431,-27.645782,53.085585,-27.640803,53.100395,-27.642046,53.115206,-27.640801,53.127548,-27.646299,53.141127,-27.65249,53.157174,-27.655916,53.173223,-27.659362,53.185176,-27.664864,53.199154,-27.670237,53.223856,-27.6818,53.233742,-27.690105,53.243631,-27.69902,53.253836,-27.707451,53.269602,-27.726544,53.279496,-27.734894,53.286925,-27.74579,53.292108,-27.758793,53.304287,-27.783357,53.30885,-27.797037,53.311754,-27.811682,53.311778,-27.824759,53.306855,-27.837417,53.29819,-27.846252,53.288339,-27.855941,53.279435,-27.864862,53.27054,-27.874712,53.26241,-27.884612,53.253765,-27.895273,53.246354,-27.904284,53.237705,-27.914519,53.22996,-27.925046,53.219553,-27.933801,53.21051,-27.941686,53.201369,-27.950214,53.191958,-27.958157,53.180822,-27.964798,53.169684,-27.971065,53.156068,-27.973668,53.138737,-27.975072,53.125119,-27.974899)',file=f)
f.close()

for i in range(0,len(x)):
    f = open(outf,'at')
    print('-Circle(',x[i],',',y[i],',',r[i],"')",sep='',file=f)
    f.close()

for i in range(0,len(ex)):
    f = open(outf,'at')
    print('-Ellipse(',ex[i],',',ey[i],',',emaj[i],"',",emin[i],"',",eang[i],")",sep='',file=f)
    f.close()

