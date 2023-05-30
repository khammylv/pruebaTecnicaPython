import numpy as np
import pydicom
from PIL import Image


im = pydicom.dcmread('rtplan.dcm')
img = im['ControlPointIndex']
print(img)