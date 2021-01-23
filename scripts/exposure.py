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

for i in range(0,162):
  file = "%d""galaxy.pi" % (i)
  hdulist = pyfits.open(file,'update')
  keys = hdulist[1].header.keys()
  if 'EXPOSURE' in keys:
    temp = hdulist[1].header['EXPOSURE']
    hdulist.close()
  else:
    temp = 0
    hdulist[1].header['EXPOSURE'] = temp
    hdulist.flush()
  file = "%d""galaxy.arf" % (i)
  hdu = pyfits.open(file, mode='update')
  hdu[1].header['EXPOSURE'] = temp
  hdu.flush()
  file = "%d""galaxy.rmf" % (i)
  f = pyfits.open(file, mode='update')
  f[1].header['EXPOSURE'] = temp
  f.flush()
  
fout = open('ciao_gal.lis', 'at')
for i in range(0,162):
  print("/raid2/dxb/xmm/analysis/CDFS/hsc/Galaxy/0108060401/""%d""galaxy.pi" % (i),file=fout)
fout.close()

arff = open('ciao_gal_arf.lis', 'at')
for i in range(0,162):
  print("/raid2/dxb/xmm/analysis/CDFS/hsc/Galaxy/0108060401/""%d""galaxy.arf" % (i),file=arff)
arff.close()

rmff = open('ciao_gal_rmf.lis', 'at')
for i in range(0,162):
  print("/raid2/dxb/xmm/analysis/CDFS/hsc/Galaxy/0108060401/""%d""galaxy.rmf" % (i),file=rmff)
rmff.close()

bkgf = open('ciao_gal_bkg.lis', 'at')
for i in range(0,162):
  print("/raid2/dxb/xmm/analysis/CDFS/hsc/Galaxy/0108060401/""%d""galaxybkg.pi" % (i),file=bkgf)
bkgf.close()



  
  
   
   
