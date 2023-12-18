from task2 import scan_annotation
from task5 import ClassedAnnotationIterator

counters = dict()
counters['TIGER'] = 0
counters['LEOPARD'] = 0


def get_next_item_path(item_class: str) -> str:
    """gives a path to next item

    Args:
        item_class (str): class that's needed 

    Returns:
        str: path for nex item
    """
    item_class = item_class.upper()
    counter = 0
    for item in data:
        if item[2].upper() == item_class:
            if counter == counters[item_class]:
                counters[item_class] += 1
                return item[1]
            else:
                counter += 1


if __name__ == "__main__":
    data = scan_annotation('annotation.csv')
    data.pop(0)
    print(get_next_item_path("LEOPARD"))
    print(get_next_item_path("LEOPARD"))
    print(get_next_item_path("TIGER"))
    print(get_next_item_path("LEOPARD"))
    print(get_next_item_path("TIGER"))
    print(get_next_item_path("LEOPARD"))
    
    a = ClassedAnnotationIterator("tiger", "annotation.csv")
    print(next(a))
