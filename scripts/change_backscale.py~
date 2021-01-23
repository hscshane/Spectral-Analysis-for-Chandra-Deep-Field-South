#!/usr/local/bin/python

import numpy
import numpy as np
import pyfits
from pyslalib import slalib
import pywcs
import math
from math import *
import re
from glob import glob

hdulist = pyfits.open('pnS005-back-full.pi')
hdulist[1].header['BACKSCAL'] = 583377871.8
hdulist.writeto('pnS005-back-full-new.pi')
hdulist.close()

