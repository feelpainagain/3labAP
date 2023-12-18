import os
import random

import cv2
import pandas as pd

from task2 import scan_annotation
from task1 import save_as_csv


def randomized_dataset_copy(dataset: list[list[str]], copy_path: str) -> list[list[str]]:
    """func that copies the dataset of pics with renaming them with random numbers

    Args:
        dataset (list[list[str]]): matrix of data without columns
        copy_path (str): path to copy

    Returns:
        list[list[str]]: new dataset
    """
    # relative or absolute
    if not os.path.exists(copy_path):
        os.mkdir(copy_path)

    img_names = set()
    result = []

    for row in dataset:
        img_class = row[-1]
        img_name = str(random.randint(0, 10000)) + '.jpg'
        while img_name in img_names:
            img_name = str(random.randint(0, 10000)) + '.jpg'
        img_names.add(img_name)

        img = cv2.imread(row[1])
        cv2.imwrite(fr'{copy_path}\{img_name}', img)
        print(row)
        print("Saved successfully")
        result.append([os.path.abspath(fr'{copy_path}\{img_name}'), fr'{copy_path}\{img_name}', img_class])
    return result

def dataset_3(annotation_path: str) -> None:
    """Creates copy of a dataset as in task 3 and creates annotation

    Args:
        annotation_path (str): Annotation of given dataset
    """
    data = scan_annotation(annotation_path)
    columns = data.pop(0)
    new_data = randomized_dataset_copy(data, 'dataset_3')
    save_as_csv(new_data, columns, 'dataset_3_annotation.csv')

# if __name__ == "__main__":
#     data = scan_annotation('annotation.csv')
#     columns = data.pop(0)
    
#     new_data = randomized_dataset_copy(data, 'task3_dataset')
#     save_as_csv(new_data, columns, 'task3_annotation.csv')
