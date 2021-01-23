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
import os

name=['0108060401','0108060501','0108060601','0108060701','0108061801','0108061901','0108062101','0108062301','0555780101','0555780201','0555780301','0555780401','0555780501','0555780601','0555780701','0555780801','0555780901','0555781001','0555782301','0604960101','0604960201','0604960301','0604960401','0604960501','0604960601','0604960701','0604960801','0604960901','0604961001','0604961101','0604961201','0604961801']

for n in name:
    for i in range(1,6):
        ct=0
        for k in range(0,163):
            file = '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/%s/redshift/grp%s/%sgalaxy.pi' % (n,i,k)
            arffile = '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/%s/redshift/grp%s/%sgalaxy.arf' % (n,i,k)
            rmffile = '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/%s/redshift/grp%s/%sgalaxy.rmf' % (n,i,k)
            txtfile = '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/%s/redshift/grp%s/%s-galaxy.txt' % (n,i,k)
            exists = os.path.isfile(file)            
            if exists and k != ct:
                outfile = '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/%s/redshift/grp%s/%sgalaxy.pi' % (n,i,ct)
                arfoutfile = '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/%s/redshift/grp%s/%sgalaxy.arf' % (n,i,ct)
                rmfoutfile = '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/%s/redshift/grp%s/%sgalaxy.rmf' % (n,i,ct)
                txtoutfile = '/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/%s/redshift/grp%s/%s-galaxy.txt' % (n,i,ct)
                os.rename(file,outfile)
                os.rename(arffile,arfoutfile)
                os.rename(rmffile,rmfoutfile)
                os.rename(txtfile,txtoutfile)
                ct+=1
            else:
                continue
               
                
