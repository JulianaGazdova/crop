# iterate through labels and paste the image with the same name into folder
import os
import shutil

LABELS = r'C:\Users\Administrator\Desktop\skola\Bc\3.rok\BP\codes\crop\test_set\test_fity_labels_5'
IMAGES = r'C:\Users\Administrator\Desktop\skola\Bc\3.rok\BP\codes\crop\test_set\test_whole_galaxies_5'
DESTINATION = r'C:\Users\Administrator\Desktop\skola\Bc\3.rok\BP\codes\crop\test_set\test_labeled_dataset_5'


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
