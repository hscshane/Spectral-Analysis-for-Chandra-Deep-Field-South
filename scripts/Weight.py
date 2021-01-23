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

weight=[]
exposure=[]

k=10
while k < 138:
  for j in range(k-10,k):
    file = "%d""galaxy.pi" % (j)
    hdulist = pyfits.open(file)
    keys = hdulist[1].header.keys()
    if 'EXPOSURE' in keys:
      x = hdulist[1].header['EXPOSURE']
      exposure.append(x)
    else:
      x = 0
      exposure.append(x)  

  numex = len(exposure)
  sumex = sum(exposure)
  avgex = sumex/10.
  
  for j in range(0,numex):
    y = exposure[j]/float(sumex)
    weight.append(y)
  
  numey = len(weight)
  
  if numex == numey:
    sumfile = open("exp.lis", 'at')
    print("first""%d"":" % (k/10), avgex, file = sumfile)
    phafile = open("%d-galaxypi.lis" % (k/10), 'at')
    print("mathpha expr='", file=phafile, end='',sep='')
    for j in range(k-10,k):  
      fout = open("%d-galaxyrmf.lis" % (k/10), 'at')
      if weight[j+10-k] != 0:
        print("%d""galaxy.rmf" % (j), weight[j+10-k],file=fout)
      else:
        continue
      fout.close()
      output = open("%d-galaxyarf.lis" % (k/10),'at')
      if weight[j+10-k] != 0:
        print("%d""galaxy.arf" % (j), weight[j+10-k],file=output)
      else:
        continue
      output.close()      
      if weight[j+10-k] != 0:
        print("%d""galaxy.pi" % (j), '+ ', file=phafile, end='')
      else:
        continue
    print("' units='c' outfil='first","%d" % (k/10),".pi' exposure='calc' areascal='%' ncomments=0" , file=phafile, sep='', end='')
    phafile.close()  
#      bkgfile = open("%d-galaxybkg.lis" % (k/10), 'at')
#      if weight[j+10-k] != 0:
#      print("%d""galaxybkg.pi" % (j), '+ ', file=bkgfile, end='')
#      else:
#	continue	
#     bkgfile.close()
  else:
    print("something went wrong")   
  k=k+10
  del weight[:]
  del exposure[:]   
else:
  for j in range(130,138):
    file = "%d""galaxy.pi" % (j)
    hdulist = pyfits.open(file)
    keys = hdulist[1].header.keys()
    if 'EXPOSURE' in keys:
      x = hdulist[1].header['EXPOSURE']
      exposure.append(x)
    else:
      x = 0
      exposure.append(x) 

  numex = len(exposure)
  sumex = sum(exposure) 
  avgex = sumex/8.
  for j in range(0,numex):
    y = exposure[j]/float(sumex)
    weight.append(y) 

  numey = len(weight) 

  if numex == numey:
    sumfile = open("exp.lis", 'at')
    print("first""%d"":" % (14), avgex, file = sumfile)
    phafile = open("%d-galaxypi.lis" % (14), 'at')
    print("mathpha expr='", file=phafile, end='',sep='')
    for j in range(130,138):  
      fout = open("%d-galaxyrmf.lis" % (14), 'at')
      print("%d""galaxy.rmf" % (j), weight[j-130],file=fout)
      fout.close()
      output = open("%d-galaxyarf.lis" % (14),'at')
      print("%d""galaxy.arf" % (j), weight[j-130],file=output)
      output.close()      
      print("%d""galaxy.pi" % (j), '+ ', file=phafile, end='')     
    print("' units='c' outfil='first","%d" % (k/10),".pi' exposure='calc' areascal='%' ncomments=0" , file=phafile, sep='', end='')
    phafile.close()
#      bkgfile = open("%d-galaxybkg.lis" % (17), 'at')
#      print("%d""galaxybkg.pi" % (j), '+ ', file=bkgfile, end='')
#      bkgfile.close()
  else:
    print("something went wrong")   
  del weight[:]
  del exposure[:]
  
sumfile = open("exp.lis")
lines = sumfile.readlines()
for i in range(0,len(lines)):
    exposure.append(float(re.split('\s+',lines[i])[1])) 
sumfile.close()
sumfile = open("exp.lis", 'at')
weight.append(sum(exposure[0:7])/7.)
weight.append(sum(exposure[7:14])/7.)
weight.append(sum(weight[0:2])/2.)
print("second1:",weight[0], file = sumfile)
print("second2:",weight[1], file = sumfile)
print("final:",weight[2], file = sumfile)
sumfile.close()
del weight[:]
del exposure[:]



sumfile = open("exp.lis")
lines = sumfile.readlines()
for i in range(0,len(lines)):
    exposure.append(float(re.split('\s+',lines[i])[1])) 
sumfile.close()
for i in range(0,7):
    weight.append(exposure[i]/sum(exposure[0:7]))
for i in range(7,14):
    weight.append(exposure[i]/sum(exposure[7:14]))
for i in range(14,16):
    weight.append(exposure[i]/sum(exposure[14:16]))

phafile = open("2-1-galaxypi.lis", 'at')
print("mathpha expr='", file=phafile, end='',sep='')
for i in range(0,7):
    fout = open("2-1-galaxyrmf.lis" , 'at')
    print("first""%d"".rmf" % (i+1), weight[i],file=fout)
    fout.close()
    output = open("2-1-galaxyarf.lis",'at')
    print("first""%d"".arf" % (i+1), weight[i],file=output)
    output.close() 
    print("first""%d"".pi" % (i+1), '+ ', file=phafile, end='')
print("' units='c' outfil='second1.pi' exposure='calc' areascal='%' ncomments=0" , file=phafile, sep='', end='')
phafile.close()

phafile = open("2-2-galaxypi.lis", 'at')
print("mathpha expr='", file=phafile, end='',sep='')
for i in range(7,14):
    fout = open("2-2-galaxyrmf.lis" , 'at')
    print("first""%d"".rmf" % (i+1), weight[i],file=fout)
    fout.close()
    output = open("2-2-galaxyarf.lis",'at')
    print("first""%d"".arf" % (i+1), weight[i],file=output)
    output.close() 
    print("first""%d"".pi" % (i+1), '+ ', file=phafile, end='')
print("' units='c' outfil='second2.pi' exposure='calc' areascal='%' ncomments=0" , file=phafile, sep='', end='')
phafile.close()

phafile = open("3-1-galaxypi.lis", 'at')
print("mathpha expr='", file=phafile, end='',sep='')
for i in range(14,16):
    fout = open("3-1-galaxyrmf.lis" , 'at')
    print("second""%d"".rmf" % (i-13), weight[i],file=fout)
    fout.close()
    output = open("3-1-galaxyarf.lis",'at')
    print("second""%d"".arf" % (i-13), weight[i],file=output)
    output.close() 
    print("second""%d"".pi" % (i-13), '+ ', file=phafile, end='')
print("' units='c' outfil='final.pi' exposure='calc' areascal='%' ncomments=0" , file=phafile, sep='', end='')
phafile.close()


