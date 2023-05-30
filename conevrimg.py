import numpy as np
import pydicom
from PIL import Image

im = pydicom.dcmread('case3a_001.dcm')

im = im.pixel_array.astype(float)

rescaled_image = (np.maximum(im,0)/im.max())*255
final_image = np.uint8(rescaled_image)

final_image = Image.fromarray(final_image)

final_image.save('new_image.jpg')


