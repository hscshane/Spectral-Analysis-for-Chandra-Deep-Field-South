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
import shutil

degtorad = math.pi / 180

sky_x = []
sky_y = []
z = []
flux = []

file='/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/0604961801-gal_redshift.txt'
f=open(file)
lines = f.readlines()
f.close()

for i in range(0,len(lines)):
  sky_x.append(float(re.split('\s+',lines[i])[0]))
  sky_y.append(float(re.split('\s+',lines[i])[1]))
  z.append(float(re.split('\s+',lines[i])[2]))
  flux.append(float(re.split('\s+',lines[i])[3]))
  

for n in range(0,140):
    x1=[]
    y1=[]
    f1=[]
    tempx=0
    tempy=0
    tempf=0
    file='/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%s-galaxy.txt' % (n)
    f=open(file)
    lines = f.readlines()
    f.close()
    x1.append(float(re.split('\s+',lines[0])[0]))
    y1.append(float(re.split('\s+',lines[0])[1]))
    f1.append(float(re.split('\s+',lines[0])[3]))    
    for i in range(0,len(z)):
        tempx = abs(sky_x[i]-x1[0])
        tempy = abs(sky_y[i]-y1[0])
        tempf = abs(abs(flux[i])-abs(f1[0]))
        if tempx <= 0.002 and tempy <= 0.002 and tempf <= 0.002:
            fout=open(file, 'at')
            print(z[i],file=fout)
            fout.close()

for n in range(0,140):
    z2=[]
    file='/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%s-galaxy.txt' % (n)
    f=open(file)
    lines = f.readlines()
    f.close()
    z2.append(float(re.split('\s+',lines[1])[0]))
    if z2[0] >= 0.0 and z2[0] <= 0.25:
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%s-galaxy.txt' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp1/%s-galaxy.txt' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.pi' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp1/%sgalaxy.pi' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.arf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp1/%sgalaxy.arf' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.rmf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp1/%sgalaxy.rmf' % (n))
    elif z2[0] > 0.25 and z2[0] <= 0.5:
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%s-galaxy.txt' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp2/%s-galaxy.txt' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.pi' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp2/%sgalaxy.pi' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.arf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp2/%sgalaxy.arf' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.rmf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp2/%sgalaxy.rmf' % (n))
    elif z2[0] > 0.5 and z2[0] <= 0.75:
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%s-galaxy.txt' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp3/%s-galaxy.txt' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.pi' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp3/%sgalaxy.pi' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.arf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp3/%sgalaxy.arf' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.rmf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp3/%sgalaxy.rmf' % (n))
    elif z2[0] > 0.75 and z2[0] <= 1.0:
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%s-galaxy.txt' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp4/%s-galaxy.txt' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.pi' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp4/%sgalaxy.pi' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.arf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp4/%sgalaxy.arf' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.rmf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp4/%sgalaxy.rmf' % (n))
    elif z2[0] > 1.0 and z2[0] <= 1.5:
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%s-galaxy.txt' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp5/%s-galaxy.txt' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.pi' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp5/%sgalaxy.pi' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.arf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp5/%sgalaxy.arf' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.rmf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp5/%sgalaxy.rmf' % (n))
    else:
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%s-galaxy.txt' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp6/%s-galaxy.txt' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.pi' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp6/%sgalaxy.pi' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.arf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp6/%sgalaxy.arf' % (n))
        shutil.copy2('/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/%sgalaxy.rmf' % (n), '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/0604961801/redshift/grp6/%sgalaxy.rmf' % (n))
       

