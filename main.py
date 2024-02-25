#==========================================
# File: main.py
# Desc: The main pyqt application script
# Created: 11/19/2023, Preston May
#
# pyright: reportMissingModuleSource=false
#==========================================

#std imports
import sys, os, pickle

#PyQt imports
from PyQt5.QtWidgets import (
  QApplication, QWidget, QLabel, QHBoxLayout,
  QVBoxLayout, QListWidget, QAbstractItemView,
  QLineEdit, QPushButton, QTextEdit,
  QToolBar, QAction, QStatusBar, QMainWindow, 
  QGridLayout, QCheckBox, QFrame, QSizePolicy,
  QMenu, QGraphicsView,
)

from PyQt5.QtGui import(
  QIcon, QIntValidator, QDrag, QPixmap
)

from PyQt5.QtCore import (
  QSize, Qt, QDate, QMimeData, pyqtSignal, QDate, QEvent
)

class MainAppWindow(QMainWindow):
  def __init__(self, parent=None):
    super().__init__()
    self.gameWindow = GameWindow()
    self.setCentralWidget(self.gameWindow)
    self.setWindowTitle("Etheria v0.1.0")


class GameWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.layout = QGridLayout()
    self.make_meta_windows()
    self.layout.addWidget(self.map, 0,0)
    self.layout.addWidget(self.inv, 0,2,2,1, Qt.AlignCenter)
    self.layout.addWidget(self.chat, 2,0,1,1,Qt.AlignBottom)
    self.setLayout(self.layout)

  def make_meta_windows(self):
    self.map = MapWindow()
    self.inv = InventoryWindow()
    self.chat = ChatWindow()


class MapWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.layout = QGridLayout()
    self.view = QGraphicsView()
    self.layout.addWidget(self.view)
    self.view.layout = QGridLayout()
    self.view.layout.addWidget(QLabel("Hello Map!"))
    self.view.setLayout(self.view.layout)
    self.setMinimumSize(400,300)
    self.setLayout(self.layout)
 

class InventoryWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.layout = QGridLayout()
    self.setFixedWidth(125)
    self.layout.addWidget(QLabel("Hello Inventory!"))
    # Add inventory 
    self.setLayout(self.layout)


class ChatWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.layout = QHBoxLayout()
    self.make_widgets()
    self.apply_layout()


  def make_widgets(self):
    self.log = QTextEdit()
    self.log.setMaximumHeight(75)

  def apply_layout(self):
    self.layout.addWidget(self.log)
    self.setLayout(self.layout)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  mainWin = MainAppWindow()
  mainWin.show()
  sys.exit(app.exec_())