import cv2
import numpy as np


def remove_frames(image_path):
    # Read the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Edge detection
    edges = cv2.Canny(gray, 30, 100)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour (outer frame)
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Crop the outer frame
    cropped_img = img[y:y + h, x:x + w]
    gray_cropped = gray[y:y + h, x:x + w]

    # Edge detection on the cropped image
    edges_cropped = cv2.Canny(gray_cropped, 30, 100)

    # Find contours on the cropped image
    contours_cropped, _ = cv2.findContours(edges_cropped, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If inner contour found, crop it
    if len(contours_cropped) > 0:
        inner_contour = max(contours_cropped, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(inner_contour)
        final_img = cropped_img[y:y + h, x:x + w]
    else:
        final_img = cropped_img

    return final_img


# Example usage:
image_path = "C:/Users/Administrator/Desktop/skola/Bc/3.rok/BP/codes/crop/testovacia_pred_edge_detection/fpC-005061-r4-0429.jpg"
result_image = remove_frames(image_path)

output_path = "C:/Users/Administrator/Desktop/skola/Bc/3.rok/BP/codes/crop/testovacia_po_edge_detection/fpC-005061-r4-0429.jpg"
cv2.imwrite(output_path, result_image)

# Save or display the result_image as required
cv2.imshow("Result Image", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()