import os

import aplpy
import cv2
import numpy as np
from PIL import Image
from astropy.io import fits
from matplotlib import pyplot as plt

# Define the paths to the FITS file and the mask in JPG format
FITS_DIR = 'C:/Users/Administrator/Desktop/skola/Bc/3.rok/BP/codes/crop/test_set/test_fity_5'
MASKS_DIR = 'C:/Users/Administrator/Desktop/skola/Bc/3.rok/BP/codes/crop/test_set/image_mask_5'
OUTPUT_DIR = 'C:/Users/Administrator/Desktop/skola/Bc/3.rok/BP/codes/crop/test_set/test_fit_coord'
FITS_FILENAMES = os.listdir(FITS_DIR)

for fit_filename in FITS_FILENAMES:
    # Open the FITS file
    with fits.open(f"{FITS_DIR}/{fit_filename}") as hdul:
        # Access the data array of the primary HDU (assuming it's the first extension)
        data = hdul[0].data

        # Open the mask image
        mask_image = Image.open(f"{MASKS_DIR}/{fit_filename.split('.')[0]}.jpg")
        # mask_image = cv2.imread(mask_file_path)
        desired_width = data.shape[1]
        desired_height = data.shape[0]

        # Resize the mask image while maintaining the original shape
        resized_mask = mask_image.resize((desired_width, desired_height), resample=Image.NEAREST)
        resized_mask.save("tmp.jpg")

        resized_mask = cv2.imread("tmp.jpg")
        resized_mask = resized_mask[:, :, 0]

        resized_mask = resized_mask[::-1]
        bin_mask = (resized_mask < 50)
        new_image = np.copy(data)
        new_image[bin_mask] = resized_mask[bin_mask]

        # Create a new FITS file to save the extracted data
        # hdu = fits.PrimaryHDU(new_image)
        # hdul_new = fits.HDUList([hdu])
        hdul_new = hdul
        hdul_new[0].data = new_image

        # Save the extracted data to a new FITS file
        # output_file_path = 'fpC-005194-g5-0367_extracted.fit'
        hdul_new.writeto(f"{OUTPUT_DIR}/{fit_filename}", overwrite=True)

        ### show before with aplpy
        gc = aplpy.FITSFigure(f"{FITS_DIR}/{fit_filename}")
        gc.show_grayscale(invert=False, stretch='power', exponent=0.5)
        plt.show()

        ### show result with aplpy
        gc = aplpy.FITSFigure(f"{OUTPUT_DIR}/{fit_filename}")
        gc.show_grayscale(invert=False, stretch='power', exponent=0.5)
        plt.show()
