import os
import numpy as np
from PIL import Image
from resizeimage import resizeimage

root = 'VAPORDATA'

imgs = []
for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        filename = os.fsdecode(filename)
        if filename.endswith(".jpg"):
            path = dirpath + '\\' + filename
            img = Image.open(path)
            img = resizeimage.resize_contain(img, [250, 250])
            new_filename = '00_' + filename
            new_path = path + new_filename

            print(new_path)
            # img.save(new_filename, img.format)
    



