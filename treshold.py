from glob import glob  # return all file paths that match a specific pattern
import os  # provides functions for creating and removing a directory (folder)
import cv2  # images
import shutil

# defining the paths to the input images and the output images
#in_dir = 'events/events_with_background'
#out_dir = 'events/events_without_background'

# read the input image file names with paths into a list
#infiles = in_dir + '/*'
#img_names = glob(infiles)
img_names = glob('./savedImage.jpg')

# loop over each input image in a for loop
for file_name in img_names:

    # read an image and convert to gray image
    im_gray = cv2.imread(file_name, 0)

    # image threshold with OTSU thresholding + getting the threshold value
    thresh, im_bw = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print("Thresh: ", thresh)

    if (thresh != 0):
        print('processing: %s...' % file_name)

        # read an input image
        src = cv2.imread(file_name, 1)
        tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

        # image threshold according to the detected threshold value
        alpha = cv2.threshold(tmp, thresh, 255, cv2.THRESH_BINARY)[1]


        # transparent background
        b, g, r = cv2.split(src)
        rgba = [b, g, r, alpha]
        dst = cv2.merge(rgba, 4)

        # write the result to disk in the previously created output directory
        size = len(os.path.basename(file_name))
        name = "Thresh_" + os.path.basename(file_name)[:size - 3] + 'jpg'
        #name = os.path.basename(file_name)[:size - 3] + 'png'
        print(name)
        #outfile = out_dir + '/' + name
        #cv2.imwrite(outfile, dst)
        cv2.imwrite(name, dst)