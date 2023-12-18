import os
import csv
import cv2
import pandas as pd

from main import save_as_csv

def scan_annotation(annotation_path: str) -> list[list[str]]:
    """func that scans annotation in given path and return data in matrix

    Args:
        annotation_path (str): path for annotation

    Returns:
        list[list[str]]: data as a matrix in return
    """
    with open(annotation_path, 'r', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
        result = []
        for row in filereader:
            row.pop(0)
            result.append(row)
        return result

def copy_dataset(dataset: list[list[str]], copy_path: str) -> list[list[str]]:
    """func that copies dataset without columns

    Args:
        dataset (list[list[str]]): data in matrix w/ columns
        copy_path (str): where to copy the data

    Returns:
        list[list[str]]: new dataset
    """
    # relative or absolute
    if not os.path.exists(copy_path):
        os.mkdir(copy_path)

    result = []

    for row in dataset:
        img_class = row[-1]
        img_name = (row[1].split('\\'))[-1]
        new_img_name = f'{img_class}_{img_name}'
        img = cv2.imread(row[1])
        cv2.imwrite(fr'{copy_path}\{new_img_name}', img)

        result.append([os.path.abspath(fr'{copy_path}\{new_img_name}'), fr'{copy_path}\{new_img_name}', img_class])
        print(row)
        print("Saved successfully")
    
    return result

if __name__ == "__main__":
    data = scan_annotation('annotation.csv')
    columns = data.pop(0)

    new_data = copy_dataset(data, 'task2_dataset')
    save_as_csv(new_data, columns, 'task2_annotation.csv')