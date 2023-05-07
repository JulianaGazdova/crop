import cv2

# img = cv2.imread("./thresh_mine.jpg")
# #np.array(img.convert("L"))
# kernel = np.ones((2, 2), np.uint8)
#
# # Using cv2.erode() method
# image = cv2.erode(img, kernel)
#
# cv2.imwrite("tresh_mine_mask.jpg", image)
#
# # Displaying the image
# cv2.imshow("dilate", image)
# cv2.waitKey(0)

image_path = r'C:\Users\Administrator\Desktop\skola\3.rok\BP\codes\crop\threshold'


# def mask_to_polygon(mask: np.array, report: bool = False) -> List[int]:
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#     polygons = []
#     for object in contours:
#         coords = []
#
#         for point in object:
#             coords.append(int(point[0][0]))
#             coords.append(int(point[0][1]))
#         polygons.append(coords)
#
#     if report:
#         print(f"Number of points = {len(polygons[0])}")
#         print(contours)
#
#     contour_mask = cv2.drawContours(mask, contours, thickness=1, color=1, contourIdx=-1)
#     cv2.imwrite("contour.jpg", contour_mask)
#
#
#     cv2.imshow('contour', contour_mask)
#     if cv2.waitKey(0) & 0xff == 27:
#         cv2.destroyAllWindows()
#
#
#     return np.array(polygons).ravel().tolist()


image = cv2.imread(fr"{image_path}\fpC-000752-g2-0301 - 0.jpg")
mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#polygons = mask_to_polygon(mask, report=True)

# *** CUSTOM SCRIPT TO TRANSFORM MASK TO YOLo

import numpy as np
from PIL import Image
# Load image mask
mask = cv2.imread(fr"{image_path}\fpC-000752-g2-0301 - 0.jpg", cv2.IMREAD_GRAYSCALE)
image = Image.open(fr"{image_path}\fpC-000752-g2-0301 - 0.jpg")
from shapely.geometry import Polygon, MultiPolygon

# Find contours
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = np.squeeze(contours[3])
from shapely.geometry import Polygon
polygon = Polygon(contours)
# Print list of points coordinates
yolo_format = "0"
coords = polygon.wkt[10:-2].split(", ")
for coord in coords:
    x, y = coord.split()
    yolo_format += " " + str(int(x) / image.width)
    yolo_format += " " + str(int(y) / image.height)

print(yolo_format)




