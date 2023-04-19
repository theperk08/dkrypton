# view.py

from PyQt6.QtCore import QSize, Qt, pyqtSlot
from PyQt6.QtWidgets import (QApplication, QGridLayout, QWidget, QMenu, QMainWindow, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton, QWidget,
QTabWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QAction

from dkrypton.view_dkrypton import Ui_MainWindow

#  GUI
class DkryptonUi(QMainWindow):
    """
    Vue principale
    """
    def __init__(self):#, model): #, controller):
        super().__init__()
        
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)        
     

    # Pour un éventuel contextMenu, quand je saurai le faire
    def cles1_remplacer(self):
        pass

    def cles2_remplacer(self):
        pass
    
    def cles1_ajouter(self):
        pass
    
    def cles2_ajouter(self):
        pass

    
