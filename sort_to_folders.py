import os
import shutil
import re
from collections import defaultdict

def sort_jpg_files_into_folders_in_directory(directory):
    groups = defaultdict(list)

    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            match = re.match(r'^fpC-(\d+)-([a-z])([\d]+)-([\d]+)\.jpg', filename)
            if match:
                num1 = match.group(1)
                num2 = match.group(3)
                num3 = match.group(4)

                folder_name = f'fpC-{num1}-x{num2}-{num3}'
                groups[folder_name].append(filename)

    # Create folders and move files
    for folder_name, filenames in groups.items():
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        for filename in filenames:
            source_path = os.path.join(directory, filename)
            destination_path = os.path.join(folder_path, filename)
            shutil.move(source_path, destination_path)


# Example usage:
directory = r"C:\Users\Administrator\Desktop\skola\Bc\3.rok\BP\codes\crop\test_set\test_whole_galaxies_sorted"
sort_jpg_files_into_folders_in_directory(directory)
