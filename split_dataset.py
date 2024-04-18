import os
import random
import re
import shutil

from typing import List

TRAIN_PATH = r'C:\Users\Administrator\Desktop\skola\Bc\3.rok\BP\codes\crop\test_set\test_labeled_dataset_5'
VAL_PATH = r'C:\Users\Administrator\Desktop\skola\Bc\3.rok\BP\codes\crop\test_set\val'
TEST_PATH = r'C:\Users\Administrator\Desktop\skola\Bc\3.rok\BP\codes\crop\test_set\test'


def get_similiar_files(filename: str, source_path: str) -> List[str]:
    match = re.match(r'^fpC-(\d+)-([a-z])([\d]+)-([\d]+)\.jpg', filename)
    group_1 = match.group(1)
    group_2 = match.group(3)
    group_3 = match.group(4)

    similiar_files = []
    files = os.listdir(source_path)
    for file in files:
        match = re.match(rf'^fpC-{group_1}-([a-z]){group_2}-{group_3}\.jpg', file)
        if match:
            similiar_files.append(file)

    return similiar_files


def split_dataset(split_index: float, source_path, destination_path):
    count = 0
    while count < split_index:
        files = os.listdir(source_path)
        file = random.choice(files)
        shutil.move(os.path.join(TRAIN_PATH, file), os.path.join(destination_path, file))
        count += 1
        similiar_files = get_similiar_files(file, TRAIN_PATH)
        for similiar_file in similiar_files:
            shutil.move(os.path.join(TRAIN_PATH, similiar_file), os.path.join(destination_path, similiar_file))
            count += 1


def create_test_val_sets(
        source_path: str, percentage_val: float, percentage_test: float, val_path: str, test_path: str
):
    files = os.listdir(source_path)
    split_index_val = int(len(files) * percentage_val)
    split_index_test = int(len(files) * percentage_test)

    split_dataset(split_index_val, source_path, val_path)
    split_dataset(split_index_test, source_path, test_path)


# get validation set
create_test_val_sets(source_path=TRAIN_PATH, percentage_val=0.33, percentage_test=0.33, val_path=VAL_PATH, test_path=TEST_PATH)
