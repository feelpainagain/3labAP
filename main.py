import sys

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

class Window(QMainWindow):

    def window(self) -> None:
        """
        Данная функция размещает элементы по макету
        """
        self.setWindowTitle("Tigers & Leopards")
        self.setWindowIcon(QIcon("icon/tigers.png"))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setStyleSheet("background-color: #FFEEDD;")

        button_tiger = QPushButton("< Next tiger", self)
        button_tiger.setFixedSize(100, 50)
        button_tiger.setStyleSheet("QPushButton {background-color: #B8B8FF}")
        button_leopard = QPushButton("Next leopard >", self)
        button_leopard.setFixedSize(100, 50)
        button_leopard.setStyleSheet("QPushButton {background-color: #B8B8FF}")

        pixmap = QPixmap("icon/main_img.jpg")
        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)
        self.lbl.setAlignment(Qt.AlignCenter)

        box = QHBoxLayout()
        box.addSpacing(1)
        box.addWidget(button_tiger)
        box.addWidget(self.lbl)
        box.addWidget(button_leopard)

        self.centralWidget.setLayout(box)

        button_tiger.clicked.connect(self.next_cat)
        button_leopard.clicked.connect(self.next_dog)

        self.folderpath = " "

        self.showMaximized()

    def create_iter(self) -> None:
        """
        Данная функция создает два объекта-итератора
        """
        self.tiger = ClassedDatasetIterator("tiger", "dataset")
        self.leopard = ClassedDatasetIterator("leopard", "dataset")

    def next_tiger(self) -> None:
        """
        Данная функция получает путь к следующему изображению tiger и размещает на экране
        """
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

    def __init__(self):
        """
        Данный конструктор вызывает методы для создания окна
        """
        super().__init__()

        self.main_window()
        self.create_iter()
        self.add_menu_bar()

    def next_leopard(self) -> None:
        """
        Данная функция получает путь к следующему изображению dog и размещает на экране
        """
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

    def add_menu_bar(self) -> None:
        """
        Данная функция создает меню и добавляет к нему действия
        """
        menu_bar = self.menuBar()

        self.file_menu = menu_bar.addMenu("&File")
        self.change_action = QAction(QIcon("icon/blue-folder.png"), "&Change dataset")
        self.change_action.triggered.connect(self.changeDataset)
        self.file_menu.addAction(self.change_action)

        self.annotation_menu = menu_bar.addMenu("&Annotation")
        self.create_annot_action = QAction(QIcon("icon/csv.png"), "&Create annotation")
        self.create_annot_action.triggered.connect(self.create_annotation)
        self.annotation_menu.addAction(self.create_annot_action)

        self.datasets_menu = menu_bar.addMenu("&Datasets")
        self.create_database_2_action = QAction(
            QIcon("icon/blue-folders.png"), "&Create dataset2"
        )
        self.create_database_2_action.triggered.connect(self.createDataset2)
        self.datasets_menu.addAction(self.create_database_2_action)

    def create_annotation(self) -> None:
        """
        Данная функция создает аннотацию для текущего dataset
        """
        if "task2_dataset" in str(self.folderpath):
            task2_annotation()
        elif "task3_dataset" in str(self.folderpath):
            task3_annotation()
        elif "dataset" in str(self.folderpath):
            annotation()

    def createDataset2(self) -> None:
        """
        Данная функция создает dataset_2
        """
        task2_dataset()
        self.create_database_3_action = QAction(
            QIcon("icon/blue-folders-stack.png"), "&Create dataset3"
        )
        self.create_database_3_action.triggered.connect(self.createDataset3)
        self.datasets_menu.addAction(self.create_database_3_action)

    def createDataset3(self) -> None:
        """
        Данная функция создает dataset_3
        """
        task3_dataset()

    def changeDataset(self) -> None:
        """
        Данная функция изменяет текущий dataset
        """
        self.folderpath = self.folderpath = QFileDialog.getExistingDirectory(
            self, "Select Folder"
        )


def main() -> None:
    """
    Данная функция создает приложение
    """
    app = QApplication(sys.argv)
    window = Window()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

