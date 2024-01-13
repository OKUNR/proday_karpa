import os
from PIL import Image

from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog,
                            QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
app = QApplication([])
win = QWidget()

win.setStyleSheet("background-color:#ABDCFF; font-size:24px; padding: 5px")
win.resize(1200, 700)
win.setWindowTitle("Easy Editor")
btn_dir = QPushButton("Papochka")
btn_dir.setCursor(Qt.PointingHandCursor)
btn_dir.setStyleSheet("border: 2px solid #708899; border-radius: 20px; background-color:white")

lw_files = QListWidget()
btn_left = QPushButton("Vleva")
btn_left.setCursor(Qt.PointingHandCursor)
btn_left.setStyleSheet("border: 2px solid #708899; border-radius: 20px; background-color:white")

btn_right = QPushButton("Vprava")
btn_right.setCursor(Qt.PointingHandCursor)
btn_right.setStyleSheet("border: 2px solid #708899; border-radius: 20px; background-color:white")

btn_flip = QPushButton("Otserkalitb")
btn_flip.setCursor(Qt.PointingHandCursor)
btn_flip.setStyleSheet("border: 2px solid #708899; border-radius: 20px; background-color:white")

btn_sharp = QPushButton("Reskostb")
btn_sharp.setCursor(Qt.PointingHandCursor)
btn_sharp.setStyleSheet("border: 2px solid #708899; border-radius: 20px; background-color:white")

btn_bw = QPushButton("ChernoBeliy")
btn_bw.setCursor(Qt.PointingHandCursor)
btn_bw.setStyleSheet("border: 2px solid #708899; border-radius: 20px; background-color:white")

lb_image = QLabel("Kartinka")
row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image)
col3.addWidget(btn_left)
col3.addWidget(btn_right)
col3.addWidget(btn_flip)
col3.addWidget(btn_sharp)

row.addLayout(col1, 20)
row.addLayout(col2, 60)
row.addLayout(col3, 20)

win.setLayout(row)

win.show()

workdir = ""
def filter (files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endwith(ext):
                result.append(filename)
    return result
def chooseWordir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensions = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]
    chooseWordir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)
btn_dir.clicked.connect(showFilenamesList)
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not (os.path.exists(path)) or os.path.isdir(path):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.stPixmap(pixmapimage)
        lb_image.show()

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)
workimage = ImageProcessor()
lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)

app.exec()