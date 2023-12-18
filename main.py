import sys

import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import (
    QApplication,
    QAction,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QWidget,
    QMainWindow,
    QPushButton,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

from task5 import ClassedAnnotationIterator, ClassedDatasetIterator
from task1 import save_as_csv, scan_dataset
from task2 import copy_dataset, scan_annotation
from task3 import randomized_dataset_copy


class MainWindow():
    class MainWindow(QMainWindow):
        def __init__(self)-> None:
            super().__init__()

            self.main_window()
            self.create_iter()

        def main_window(self) -> None:
            """
            Данная функция размещает элементы по макету
            """
            self.setWindowTitle("Images Cats and Dogs")
            self.setWindowIcon(QIcon("icon/cat_dog.png"))
            self.centralWidget = QWidget()
            self.setCentralWidget(self.centralWidget)
            self.setStyleSheet("background-color: #FFFFFF;")

            button_horse = QPushButton("Next horse", self)
            button_horse.setFixedSize(300, 150)
            button_horse.setStyleSheet("QPushButton")
            button_zebra = QPushButton("Next zebra", self)
            button_zebra.setFixedSize(300, 150)
            button_zebra.setStyleSheet("QPushButton")

            pixmap = QPixmap()
            self.lbl = QLabel(self)
            self.lbl.setPixmap(pixmap)
            self.lbl.setAlignment(Qt.AlignCenter)

            box = QHBoxLayout()
            box.addSpacing(1)
            box.addWidget(button_horse)
            box.addWidget(self.lbl)
            box.addWidget(button_zebra)

            self.centralWidget.setLayout(box)

            button_horse.clicked.connect(self.next_cat)
            button_zebra.clicked.connect(self.next_dog)

            self.folderpath = " "
            self.showMaximized()


        def create_iter(self) -> None:
            self.cat = ClassedDatasetIterator("bay horse", ["dataset\\bay horse"])
            self.dog = ClassedDatasetIterator("zebra", ["dataset\\zebra"])

        def next_cat(self) -> None:
            lbl_size = self.lbl.size()
            next_image = next(self.cat)
            if next_image != None:
                img = QPixmap(next_image).scaled(
                    lbl_size, aspectRatioMode=Qt.KeepAspectRatio
                )
                self.lbl.setPixmap(img)
                self.lbl.setAlignment(Qt.AlignCenter)
            else:
                self.create_iter()
                self.next_cat()

        def next_dog(self) -> None:
            lbl_size = self.lbl.size()
            next_image = next(self.dog)
            if next_image != None:
                img = QPixmap(next_image).scaled(
                    lbl_size, aspectRatioMode=Qt.KeepAspectRatio
                )
                self.lbl.setPixmap(img)
                self.lbl.setAlignment(Qt.AlignCenter)
            else:
                self.create_iter()
                self.next_dog()




def main() -> None:

    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()