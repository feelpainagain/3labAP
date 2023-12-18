from typing import Optional

from task1 import scan_dataset
from task2 import scan_annotation
    
class ClassedDatasetIterator:
    data = []
    def __init__(self, class_name: str, dataset_paths: list[str]) -> None:
        """func that iterates through dataset, returning items

        Args:
            class_name (str): class to work with
            annotation_path (str): dataset path
        """
        self.counter = 0
        self.class_name = class_name
        self.data = scan_dataset(dataset_paths)
        self.limit = len(self.data)

    def __iter__(self):
        """returns the iterator object 
        """
        return self
        
    def __next__(self) -> Optional[str]:
        """Returns next image of Iterator's class

        Returns:
            Optional[str]: returns  abs path to pic or None
        """
        while self.counter < self.limit:
            if self.data[self.counter][-1].upper() == self.class_name.upper():
                self.counter += 1
                return self.data[self.counter - 1][0]
            self.counter += 1
        raise StopIteration


if __name__ == '__main__':
    
    s_iter2 = ClassedDatasetIterator("tiger", ["dataset\\tiger", "dataset\\leopard"])
    print(next(s_iter2))
    print(next(s_iter2))
    print(next(s_iter2))