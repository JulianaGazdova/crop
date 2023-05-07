import os
import cv2
import shutil
import numpy as np

mask_path = os.path.normpath(r'C:\Users\Administrator\Desktop\skola\3.rok\BP\codes\crop\resized_50')
image_path = os.path.normpath(r'C:\Users\Administrator\Desktop\skola\3.rok\BP\codes\crop\cropped_galaxies')
dest_path = os.path.normpath(r'C:\Users\Administrator\Desktop\skola\3.rok\BP\codes\crop\full_masks')


images = os.listdir(mask_path)

for image_file in images:
    image_name = image_file.split(" ")[0]
    image = cv2.imread(fr"{image_path}\{image_name}.jpg")
    height, width, _ = image.shape
    black_image = np.zeros((height, width), dtype = np.uint8)
    cv2.imshow('black image', black_image)


    #shutil.copy(fr"{image_path}\{image_name}.jpg", dest_path)


