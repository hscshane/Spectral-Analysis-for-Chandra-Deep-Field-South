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

t1=pyfits.open('pnS005-bkg_region-sky-new.fits')
t2=pyfits.open('pnS005-bkg_region-sky-original.fits')
nrows1=t1[1].data.shape[0]
nrows2=t2[1].data.shape[0]
num=nrows1 + nrows2
hdu=pyfits.BinTableHDU.from_columns(t1[1].columns, nrows=num)
for colname in t1[1].columns.names:
	hdu.data[colname][nrows1:] = t2[1].data[colname]
nhdu1 = pyfits.PrimaryHDU()
nhdu1.header = t1[0].header
hdu.header = t1[1].header
hdu.header['NAXIS2']= num
hdulist = pyfits.HDUList([nhdu1,hdu])
hdulist.writeto('pnS005-bkg_region-sky.fits')
t1.close()
t2.close()


t1=pyfits.open('pnS005-bkg_region-det-new.fits')
t2=pyfits.open('pnS005-bkg_region-det-original.fits')
nrows1=t1[1].data.shape[0]
nrows2=t2[1].data.shape[0]
num=nrows1 + nrows2
hdu=pyfits.BinTableHDU.from_columns(t1[1].columns, nrows=num)
for colname in t1[1].columns.names:
	hdu.data[colname][nrows1:] = t2[1].data[colname]
nhdu1 = pyfits.PrimaryHDU()
nhdu1.header = t1[0].header
hdu.header = t1[1].header
hdu.header['NAXIS2']= num
hdulist = pyfits.HDUList([nhdu1,hdu])
hdulist.writeto('pnS005-bkg_region-det.fits')
t1.close()
t2.close()
