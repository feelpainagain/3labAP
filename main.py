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

            button_tiger = QPushButton("Next tiger", self)
            button_tiger.setFixedSize(300, 150)
            button_tiger.setStyleSheet("QPushButton")
            button_leopard = QPushButton("Next leopard", self)
            button_leopard.setFixedSize(300, 150)
            button_leopard.setStyleSheet("QPushButton")

            pixmap = QPixmap()
            self.lbl = QLabel(self)
            self.lbl.setPixmap(pixmap)
            self.lbl.setAlignment(Qt.AlignCenter)

            box = QHBoxLayout()
            box.addSpacing(1)
            box.addWidget(button_tiger)
            box.addWidget(self.lbl)
            box.addWidget(button_leopard)

            self.centralWidget.setLayout(box)

            button_tiger.clicked.connect(self.next_tiger)
            button_leopard.clicked.connect(self.next_leopard)

            self.folderpath = " "
            self.showMaximized()


        def create_iter(self) -> None:
            self.tiger = ClassedDatasetIterator("tiger", ["dataset\\tiger"])
            self.leopard = ClassedDatasetIterator("leopard", ["dataset\\leopard"])

        def next_tiger(self) -> None:
            lbl_size = self.lbl.size()
            next_image = next(self.tiger)
            if next_image != None:
                img = QPixmap(next_image).scaled(
                    lbl_size, aspectRatioMode=Qt.KeepAspectRatio
                )
                self.lbl.setPixmap(img)
                self.lbl.setAlignment(Qt.AlignCenter)
            else:
                self.create_iter()
                self.next_tiger()

        def next_leopard(self) -> None:
            lbl_size = self.lbl.size()
            next_image = next(self.leopard)
            if next_image != None:
                img = QPixmap(next_image).scaled(
                    lbl_size, aspectRatioMode=Qt.KeepAspectRatio
                )
                self.lbl.setPixmap(img)
                self.lbl.setAlignment(Qt.AlignCenter)
            else:
                self.create_iter()
                self.next_leopard()




def main() -> None:

    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()