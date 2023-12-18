import sys
import os

from PyQt5.QtWidgets import (
    QApplication,
    QAction,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QWidget,
    QMainWindow,
    QPushButton,
    QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

from task5 import ClassedAnnotationIterator, ClassedDatasetIterator
from task1 import save_as_csv, scan_dataset
from task2 import copy_dataset, scan_annotation, dataset_2
from task3 import randomized_dataset_copy, dataset_3


class Window(QMainWindow):
    def __init__(self):
        """
        makes window
        """
        super().__init__()

        self.main_window()
        self.create_iter()
        self.add_menu_bar()

    def main_window(self) -> None:
        """
        placing elements on workspace
        """
        self.setWindowTitle("Tigers and leopards")
        self.setWindowIcon(QIcon())
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setStyleSheet("background-color: #74992e;")

        button_tiger = QPushButton(" Next tiger", self)
        button_tiger.setFixedSize(500, 50)
        button_tiger.setStyleSheet("QPushButton {background-color: #bbff00}")
        button_leopard = QPushButton("Next leopard ", self)
        button_leopard.setFixedSize(500, 50)
        button_leopard.setStyleSheet("QPushButton {background-color: #bbff00}")

        pixmap = QPixmap()
        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)
        self.lbl.setAlignment(Qt.AlignCenter)

        box = QHBoxLayout()
        box.addSpacing(3)
        box.addWidget(button_tiger)
        box.addWidget(self.lbl)
        box.addWidget(button_leopard)

        self.centralWidget.setLayout(box)

        button_tiger.clicked.connect(self.next_tiger)
        button_leopard.clicked.connect(self.next_leopard)

        self.folderpath = ""

        self.showMaximized()

    def create_iter(self) -> None:
        """
        makes two iterators
        """
        self.tiger = ClassedDatasetIterator("tiger", [r"dataset\tiger"])
        self.leopard = ClassedDatasetIterator("leopard", [r"dataset\leopard"])

    def next_tiger(self) -> None:
        """
        Данная функция получает путь к следующему изображению тигра и размещает её на экране
        """
        lbl_size = self.lbl.size()
        try: 
            next_image = next(self.tiger)
        except StopIteration:
            next_image = None

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
        """
        Данная функция получает путь к следующему изображению леопарда и размещает её на экране
        """
        lbl_size = self.lbl.size()
        try: 
            next_image = next(self.leopard)
        except StopIteration:
            next_image = None

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
        self.change_action = QAction(QIcon(), "&Choose dataset")
        self.change_action.triggered.connect(self.chooseDataset)
        self.file_menu.addAction(self.change_action)

        self.annotation_menu = menu_bar.addMenu("&Annotation")
        self.create_annot_action = QAction(QIcon(), "&Create annotation")
        self.create_annot_action.triggered.connect(self.create_annotation)
        self.annotation_menu.addAction(self.create_annot_action)

        self.datasets_menu = menu_bar.addMenu("&Datasets")

    def create_annotation(self) -> None:
        """
        Данная функция создает аннотацию для исходного dataset
        """
        dataset_path = str(self.folderpath)
        dataset_path = dataset_path.replace('/', '\\')
        dataset_name = dataset_path.split('\\')[-1]

        self.dataset_name = dataset_name
        if os.path.exists(dataset_path + "\\tiger") and os.path.exists(dataset_path + "\\leopard"):
            data = scan_dataset([dataset_name + "\\tiger", dataset_name + "\\leopard"])
            save_as_csv(data, ["Abs Path", "Rel Path", "Item Class"], dataset_name + "_annotation.csv")
            
            self.create_database_2_action = QAction(
                QIcon(), "&Create dataset2"
            )
            self.create_database_2_action.triggered.connect(self.createDataset2)
            self.datasets_menu.addAction(self.create_database_2_action)

            self.create_database_3_action = QAction(
            QIcon(), "&Create dataset3"
            )
            self.create_database_3_action.triggered.connect(self.createDataset3)
            self.datasets_menu.addAction(self.create_database_3_action)
        else: 
            print("Выбранная папка не соответствует исходному датасету по формату!")
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Выбранная папка не соответствует исходному датасету по формату!")
            msg.setIcon(QMessageBox.Warning)

            msg.exec_()


    def createDataset2(self) -> None:
        """
        Данная функция создает dataset_2
        """
        dataset_2(self.dataset_name + "_annotation.csv")

    def createDataset3(self) -> None:
        """
        Данная функция создает dataset_3
        """
        dataset_3(self.dataset_name + "_annotation.csv")

    def chooseDataset(self) -> None:
        """
        Данная функция изменяет выбор папки исходного dataset
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
