#!/usr/local/bin/python

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

xmm_src = 'XMM_fk5.reg'
fin_src = 'FinoguenovCluster_fk5.reg'
chandra_src = 'Chandra_fk5.reg'
f = open(xmm_src)
xmm_lines = f.readlines()
f.close()
f = open(fin_src)
fin_lines = f.readlines()
f.close()
f = open(chandra_src)
chandra_lines = f.readlines()
f.close()

xmm_ra =[]
xmm_dec = []
xmm_r = []
fin_ra = []
fin_dec = []
fin_maj = []
fin_min = []
fin_angle = []
chandra_ra =[]
chandra_dec = []
chandra_r = []
for i in range(0,len(xmm_lines)):
  xmm_ra.append(float(re.split('\s+',xmm_lines[i])[0]))
  xmm_dec.append(float(re.split('\s+',xmm_lines[i])[1]))
  xmm_r.append(float(re.split('\s+',xmm_lines[i])[2]))

for i in range(0,len(chandra_lines)):
  chandra_ra.append(float(re.split('\s+',chandra_lines[i])[0]))
  chandra_dec.append(float(re.split('\s+',chandra_lines[i])[1]))
  chandra_r.append(float(re.split('\s+',chandra_lines[i])[2]))

for i in range(0,len(fin_lines)):
  fin_ra.append(float(re.split('\s+',fin_lines[i])[0]))
  fin_dec.append(float(re.split('\s+',fin_lines[i])[1]))
  fin_maj.append(float(re.split('\s+',fin_lines[i])[2]))
  fin_min.append(float(re.split('\s+',fin_lines[i])[3]))
  fin_angle.append(float(re.split('\s+',fin_lines[i])[4]))

naxis1 = 900
naxis2 = 900
keyword=['CTYPE1','CRVAL1','CRPIX1','CDELT1','CUNIT1','CTYPE2','CRVAL2','CRPIX2','CDELT2','CUNIT2']
#for i in range(0,len(lines)):
for i in range(0,len(lines)):
  file = "./"+id[i]+"_mask_all_04_06.fits"
  print(file)
  hdu = pyfits.open(file)
  header = hdu[0].header
  data = hdu[0].data
  wcs = pywcs.WCS(naxis=2)
  wcs.wcs.crpix = [header['CRPIX1'], header['CRPIX2']]
  wcs.wcs.cdelt = np.array([header['CDELT1'], header['CDELT2']])
  wcs.wcs.crval = [header['CRVAL1'], header['CRVAL2']]
  wcs.wcs.ctype = [header['CTYPE1'], 	header['CTYPE2']]
  pixscale = float(header['CDELT2'])

  for pixy in range(0,naxis1):
    for pixx in range(0,naxis2):
      if data[pixy][pixx] != 0:
        for k in range(0,len(chandra_lines)):
          skycoord = np.array([[chandra_ra[k],chandra_dec[k]]])
          pixcoord = wcs.wcs_sky2pix(skycoord,1)
          radius = ((pixcoord[0][0]-pixx-1)**2+(pixcoord[0][1]-pixy-1)**2)**0.5*pixscale*3600
          if radius <= chandra_r[k] :
            data[pixy][pixx] = 0

  #maskfile = id[i]+"_mask_allsrc_04_06.fits"
  maskfile ="mask_allsrc_04_06.fits"
  nhdu = pyfits.PrimaryHDU(data)
  for i in range(0,len(keyword)):
    nhdu.header[keyword[i]]=header[keyword[i]]
  nhdulist = pyfits.HDUList(nhdu)
  nhdulist.writeto(maskfile)
  hdu.close() 

