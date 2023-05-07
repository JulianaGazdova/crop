# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open("./fpC-000752-g2-0314.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left = int(0.85584 * width)
top = int(0.06447 * height)
right = int(((left/width) + 0.04309) * width)
bottom = int(((top/height) + 0.61555) * height)

# Cropped image of above dimension
# (It will not change original image)
print(f"Height: {height}, Width: {width}\nleft: {left}\ntop: {top}\nright: {right}\nbottom: {bottom}")
im1 = im.crop((left, top, right, bottom))

# Shows the image in image viewer
im1.show()
