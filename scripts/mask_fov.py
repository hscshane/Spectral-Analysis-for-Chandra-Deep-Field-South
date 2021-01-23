#!/usr/bin/python

from __future__ import print_function
import numpy as np
import pyfits
from pyslalib import slalib
import pywcs
import math
import re
from glob import glob

degtorad = math.pi/180

file = 'obs_id'
f = open(file)
lines = f.readlines()
f.close()
id = []
for i in range(0,len(lines)):
  id.append(re.split('\s+',lines[i])[0])
  print(id[i])

fov = "exposure_all_04_06_threshold.fits"
keyword=['HDUVERS', 'HDUCLASS', 'HDUCLAS1', 'HDUCLAS2','CTYPE1','CRVAL1','CRPIX1','CDELT1','CUNIT1','CTYPE2','CRVAL2','CRPIX2','CDELT2','CUNIT2']

hdufov = pyfits.open(fov)
fovdata = hdufov[0].data
fovhdr = hdufov[0].header
nwcs = pywcs.WCS(naxis=2)
nwcs.wcs.crpix = [fovhdr['CRPIX1'], fovhdr['CRPIX2']]
nwcs.wcs.cdelt = np.array([fovhdr['CDELT1'], fovhdr['CDELT2']])
nwcs.wcs.crval = [fovhdr['CRVAL1'], fovhdr['CRVAL2']]
nwcs.wcs.ctype = [fovhdr['CTYPE1'], fovhdr['CTYPE2']]


naxis1 = 900
naxis2 = 900
keyword=['CTYPE1','CRVAL1','CRPIX1','CDELT1','CUNIT1','CTYPE2','CRVAL2','CRPIX2','CDELT2','CUNIT2']
#for i in range(0,len(lines)):
for i in range(0,len(lines)):
  mask = np.zeros((naxis1,naxis2))
  file = "../"+id[i]+"/"+"pnS005-exp-im-400-600.fits"
  print(file)
  hdu = pyfits.open(file)
  header = hdu[0].header
  data = hdu[0].data
  wcs = pywcs.WCS(naxis=2)
  wcs.wcs.crpix = [header['CRPIX1'], header['CRPIX2']]
  wcs.wcs.cdelt = np.array([header['CDELT1'], header['CDELT2']])
  wcs.wcs.crval = [header['CRVAL1'], header['CRVAL2']]
  wcs.wcs.ctype = [header['CTYPE1'], header['CTYPE2']]
  for pixy in range(0,naxis1):
    for pixx in range(0,naxis2):
      pixcoord = np.array([[pixx+1,pixy+1]])
      skycoord = wcs.wcs_pix2sky(pixcoord,1)
#        (skyx,skyy) = slalib.sla_fk45z(skycoord[0][0]*degtorad,skycoord[0][1]*degtorad,1950.)
#      nskycoord = np.array([[skyx/degtorad,skyy/degtorad]])
      npixcoord = nwcs.wcs_sky2pix(skycoord,1)
      npixx = round(npixcoord[0][0])
      npixy = round(npixcoord[0][1])
#        print (pixx,pixy),(npixx,npixy)
      if npixx < naxis1 and npixy < naxis2:
        if fovdata[npixy][npixx] > 0:
          mask[pixy][pixx] = 1
      else:
        mask[pixy][pixx] = 0
  maskfile = id[i]+"_mask_04_06.fits"
  nhdu = pyfits.PrimaryHDU(mask)
  for i in range(0,len(keyword)):
    nhdu.header[keyword[i]]=header[keyword[i]]
  nhdulist = pyfits.HDUList(nhdu)
  nhdulist.writeto(maskfile)
  hdu.close() 

