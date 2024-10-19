import os
import shutil

LABELS = "false_positive/fp_annotations"
IMAGES = 'false_positive/images_without_border'
DESTINATION = 'false_positive/fp_images'


def copy_image(image_name: str):
    image_path = os.path.join(IMAGES, image_name + '.jpg')
    # copy image from IMAGES to DESTINATION
    shutil.copy(image_path, DESTINATION)


def create_labeled_dataset():
    labels = os.listdir(LABELS)
    for label in labels:
        label_name = label.split('.')[0]
        copy_image(label_name)

create_labeled_dataset()