import os
import cv2
from PIL import Image

image_path = os.path.normpath(r'C:\Users\Administrator\Desktop\skola\3.rok\BP\codes\crop\good_masks')
dest_path = os.path.normpath(r'C:\Users\Administrator\Desktop\skola\3.rok\BP\codes\crop\resized_50')

images = os.listdir(image_path)

for image_file in images:
    image = cv2.imread(fr"{image_path}\{image_file}")
    # cv2.imshow('image', image)

    resized_image = cv2.resize(image, (50, 50))
    #cv2.imshow('resized', resized_image)

    #if cv2.waitKey(0) & 0xff == 27:
    #    cv2.destroyAllWindows()

    cv2.imwrite(os.path.join(dest_path, image_file), resized_image)

