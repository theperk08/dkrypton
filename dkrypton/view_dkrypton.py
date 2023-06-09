# Form implementation generated from reading ui file 'main_dkrypton.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from pyqtgraph import PlotWidget, BarGraphItem, plot
import pyqtgraph as pg
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure
import random
import numpy as np


class Window_Graph(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
 
        # a figure instance to plot on
        self.figure = Figure(figsize=(15,2))
        
 
        # création du canvas contenant la figure
        self.canvas = FigureCanvasQTAgg(self.figure)

        # on initialise toute de suite une figure
        # qu'on pourra effacer à chaque appel
        self.ax = self.figure.add_subplot(111, position=[0.05, 0.12, 0.85, 0.78]) #gauche, bas, large, haut
        
        
        layout = QtWidgets.QVBoxLayout()     
        layout.addWidget(self.canvas)        
        self.setLayout(layout)

    def efface(self):
        # pour effacer l'ancienne figure        
        self.ax.clear()             
       
 
    def plot(self, data_x, data_y, data_y2, data_y3):

        # on efface d'abord l'ancien graphique
        self.efface()
        
        # on dessine la nouvelle
        nombres = np.arange(len(data_x))
        width = 0.30
        
        self.ax.bar(nombres - width, data_y, width, label = 'crypté', color = 'red')
        self.ax.bar(nombres , data_y2, width, label = 'théorique', color = 'blue')
        self.ax.bar(nombres + width, data_y3, width, label = 'décrypté', color = 'green')
        self.ax.set_xticks(nombres)

        self.ax.set_xticklabels(list(data_x))
        #self.ax.tick_params(pad = 15)
                        
        self.ax.legend()
        self.ax.set_title('Distribution des fréquences (en %) dans le texte')
 
        # on rafraîchit l'affichage
        self.canvas.draw()
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        x1 = 10
        x2 = 150
        x3 = 360
        x4 = 500
        x5 = 600
        x6 = 800

        y2 = 350
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1190, 750))
        self.tabWidget.setObjectName("tabWidget")


        # onglet crypto classique
        self.tab_cc = QtWidgets.QWidget()
        self.tab_cc.setObjectName("tab_cc")
        
        self.label_cc_alpha = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_alpha.setGeometry(QtCore.QRect(x1, 20, 50, 20))
        self.label_cc_alpha.setObjectName("label_cc_alpha")        
        self.lineEdit_cc_alpha = QtWidgets.QLineEdit(parent=self.tab_cc)
        self.lineEdit_cc_alpha.setGeometry(QtCore.QRect(x2, 20, 200, 20))
        self.lineEdit_cc_alpha.setObjectName("lineEdit_cc_alpha")
        self.lineEdit_cc_alpha.setStyleSheet("font-family: Courier")
        
        self.label_cc_alphaw = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_alphaw.setGeometry(QtCore.QRect(x1, 40, 60, 20))
        self.label_cc_alphaw.setObjectName("label_cc_alphaw")
        self.lineEdit_cc_alphaw = QtWidgets.QLineEdit(parent=self.tab_cc)
        self.lineEdit_cc_alphaw.setGeometry(QtCore.QRect(x2, 40, 200, 20))
        self.lineEdit_cc_alphaw.setObjectName("lineEdit_cc_alphaw")
        self.lineEdit_cc_alphaw.setStyleSheet("font-family: Courier")
        
        self.label_cc_crypto = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_crypto.setGeometry(QtCore.QRect(x1, 80, 47, 20))
        self.label_cc_crypto.setObjectName("label_cc_crypto")
        self.label_cc_crypto.setStyleSheet("background-color: aqua")        
        self.combo_cc_crypto = QtWidgets.QComboBox(parent=self.tab_cc)
        self.combo_cc_crypto.setGeometry(QtCore.QRect(x2, 80, 231, 22))
        self.combo_cc_crypto.setObjectName("combo_cc_crypto")
        self.combo_cc_crypto.setStyleSheet("font-family: Courier")
        self.combo_cc_crypto.setEditable(True)
        
        self.label_cc_cle1 = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_cle1.setGeometry(QtCore.QRect(x1, 110, 47, 20))
        self.label_cc_cle1.setObjectName("label_cc_cle1")
        self.label_cc_cle1.setStyleSheet("background-color: greenyellow")
        self.combo_cc_cle1 = QtWidgets.QComboBox(parent=self.tab_cc)
        self.combo_cc_cle1.setGeometry(QtCore.QRect(x2, 110, 231, 22))
        self.combo_cc_cle1.setObjectName("combo_cc_cle1")
        self.combo_cc_cle1.setStyleSheet("font-family: Courier")
        self.combo_cc_cle1.setEditable(True)
        
        self.label_cc_cle2 = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_cle2.setGeometry(QtCore.QRect(x1, 140, 47, 20))
        self.label_cc_cle2.setObjectName("label_cc_cle2")
        self.label_cc_cle2.setStyleSheet("background-color: lightgreen")
        self.combo_cc_cle2 = QtWidgets.QComboBox(parent=self.tab_cc)
        self.combo_cc_cle2.setGeometry(QtCore.QRect(x2, 140, 231, 22))
        self.combo_cc_cle2.setObjectName("combo_cc_cle2")
        self.combo_cc_cle2.setStyleSheet("font-family: Courier")
        self.combo_cc_cle2.setEditable(True)
        
        self.label_cc_cle3 = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_cle3.setGeometry(QtCore.QRect(x1, 170, 47, 20))
        self.label_cc_cle3.setObjectName("label_cc_cle3")
        self.label_cc_cle3.setStyleSheet("background-color: seagreen")
        self.combo_cc_cle3 = QtWidgets.QComboBox(parent=self.tab_cc)
        self.combo_cc_cle3.setGeometry(QtCore.QRect(x2, 170, 231, 22))
        self.combo_cc_cle3.setObjectName("combo_cc_cle3")
        self.combo_cc_cle3.setStyleSheet("font-family: Courier")
        self.combo_cc_cle3.setEditable(True)
        
        self.label_cc_cle4 = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_cle4.setGeometry(QtCore.QRect(x1, 200, 47, 20))
        self.label_cc_cle4.setObjectName("label_cc_cle4")
        self.label_cc_cle4.setStyleSheet("background-color: olivedrab")
        self.combo_cc_cle4 = QtWidgets.QComboBox(parent=self.tab_cc)
        self.combo_cc_cle4.setGeometry(QtCore.QRect(x2, 200, 231, 22))
        self.combo_cc_cle4.setObjectName("combo_cc_cle4")
        self.combo_cc_cle4.setStyleSheet("font-family: Courier")
        self.combo_cc_cle4.setEditable(True)
                
        self.pushButton_cc_Go = QtWidgets.QPushButton(parent=self.tab_cc)
        self.pushButton_cc_Go.setGeometry(QtCore.QRect(250, 240, 75, 23))
        self.pushButton_cc_Go.setObjectName("pushButton_cc_Go")
        self.pushButton_cc_Go.setStyleSheet("background-color: dodgerblue")

        self.label_cc_vigenere = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_vigenere.setGeometry(QtCore.QRect(x1, 280, 100, 35))
        self.label_cc_vigenere.setObjectName("label_cc_vigenere")
        self.label_cc_vigenere.setStyleSheet("background-color: sandybrown")
        self.label_cc_vigenere.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEdit_cc_vigenere = QtWidgets.QLineEdit(parent=self.tab_cc)
        self.lineEdit_cc_vigenere.setGeometry(QtCore.QRect(x2, 290, 231, 20))
        self.lineEdit_cc_vigenere.setReadOnly(True)
        self.lineEdit_cc_vigenere.setObjectName("lineEdit_cc_vigenere")
        self.lineEdit_cc_vigenere.setStyleSheet("font-family: Courier")
        
        self.label_cc_cryptoplus = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_cryptoplus.setGeometry(QtCore.QRect(x1, 350, 70, 20))
        self.label_cc_cryptoplus.setObjectName("label_cc_cryptoplus")
        self.label_cc_cryptoplus.setStyleSheet("background-color: yellow")
        self.combo_cc_cryptoplus = QtWidgets.QComboBox(parent=self.tab_cc)
        self.combo_cc_cryptoplus.setGeometry(QtCore.QRect(x2, 350, 231, 22))
        self.combo_cc_cryptoplus.setObjectName("combo_cc_cryptoplus")
        self.combo_cc_cryptoplus.setStyleSheet("font-family: Courier")
        
        self.label_cc_cryptomoins = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_cryptomoins.setGeometry(QtCore.QRect(x1, 380, 70, 20))
        self.label_cc_cryptomoins.setObjectName("label_cc_cryptomoins")
        self.label_cc_cryptomoins.setStyleSheet("background-color: yellow")
        self.combo_cc_cryptomoins = QtWidgets.QComboBox(parent=self.tab_cc)
        self.combo_cc_cryptomoins.setGeometry(QtCore.QRect(x2, 380, 231, 22))
        self.combo_cc_cryptomoins.setObjectName("combo_cc_cryptomoins")
        self.combo_cc_cryptomoins.setStyleSheet("font-family: Courier")

        self.label_cc_beaufortall = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_beaufortall.setGeometry(QtCore.QRect(x1, 430, 100, 35))
        self.label_cc_beaufortall.setObjectName("label_cc_beaufort_all")
        self.label_cc_beaufortall.setStyleSheet("background-color: sandybrown")
        self.lineEdit_cc_beaufortall = QtWidgets.QLineEdit(parent=self.tab_cc)
        self.lineEdit_cc_beaufortall.setGeometry(QtCore.QRect(x2, 440, 231, 22))
        self.lineEdit_cc_beaufortall.setObjectName("combo_cc_beaufort_all")
        self.lineEdit_cc_beaufortall.setStyleSheet("font-family: Courier")

        self.label_cc_beaufort = QtWidgets.QLabel(parent=self.tab_cc)
        self.label_cc_beaufort.setGeometry(QtCore.QRect(x1, 480, 100, 35))
        self.label_cc_beaufort.setObjectName("label_cc_beaufort")
        self.label_cc_beaufort.setStyleSheet("background-color: sandybrown")
        self.lineEdit_cc_beaufort = QtWidgets.QLineEdit(parent=self.tab_cc)
        self.lineEdit_cc_beaufort.setGeometry(QtCore.QRect(x2, 490, 231, 22))
        self.lineEdit_cc_beaufort.setObjectName("combo_cc_beaufort")
        self.lineEdit_cc_beaufort.setStyleSheet("font-family: Courier")               
       

        # onglet crypto sans clé
        self.tab_csc = QtWidgets.QWidget()
        self.tab_csc.setObjectName("tab_csc")

        self.label_csc_alpha = QtWidgets.QLabel(parent=self.tab_csc)
        self.label_csc_alpha.setGeometry(QtCore.QRect(x1, 20, 47, 20))
        self.label_csc_alpha.setObjectName("label_csc_alpha")

        self.lineEdit_csc_alpha = QtWidgets.QLineEdit(parent=self.tab_csc)
        self.lineEdit_csc_alpha.setGeometry(QtCore.QRect(x2, 20, 200, 20))
        self.lineEdit_csc_alpha.setObjectName("lineEdit_csc_alpha")
        self.lineEdit_csc_alpha.setStyleSheet("font-family: Courier")
        
        self.label_csc_alphaw = QtWidgets.QLabel(parent=self.tab_csc)
        self.label_csc_alphaw.setGeometry(QtCore.QRect(x1, 40, 47, 20))
        self.label_csc_alphaw.setObjectName("label_csc_alphaw")
        self.lineEdit_csc_alphaw = QtWidgets.QLineEdit(parent=self.tab_csc)
        self.lineEdit_csc_alphaw.setGeometry(QtCore.QRect(x2, 40, 200, 20))
        self.lineEdit_csc_alphaw.setObjectName("lineEdit_csc_alphaw")
        self.lineEdit_csc_alphaw.setStyleSheet("font-family: Courier")
        
        self.label_csc_crypto = QtWidgets.QLabel(parent=self.tab_csc)
        self.label_csc_crypto.setGeometry(QtCore.QRect(x1, 80, 47, 20))
        self.label_csc_crypto.setObjectName("label_csc_crypto")        
        self.combo_csc_crypto = QtWidgets.QComboBox(parent=self.tab_csc)
        self.combo_csc_crypto.setGeometry(QtCore.QRect(x2, 80, 300, 22))
        self.combo_csc_crypto.setObjectName("combo_csc_crypto")
        self.combo_csc_crypto.setEditable(True)
        self.combo_csc_crypto.setStyleSheet("font-family: Courier")

        self.pushButton_csc_Go = QtWidgets.QPushButton(parent=self.tab_csc)
        self.pushButton_csc_Go.setGeometry(QtCore.QRect(250, 110, 75, 23))
        self.pushButton_csc_Go.setObjectName("pushButton_csc_Go")
        self.pushButton_csc_Go.setStyleSheet("background-color: dodgerblue")
        
        self.label_csc_cesar = QtWidgets.QLabel(parent=self.tab_csc)
        self.label_csc_cesar.setGeometry(QtCore.QRect(x1, 150, 47, 20))
        self.label_csc_cesar.setObjectName("label_csc_cesar")       
        self.combo_csc_cesar = QtWidgets.QComboBox(parent=self.tab_csc)
        self.combo_csc_cesar.setGeometry(QtCore.QRect(x2, 150, 300, 22))
        self.combo_csc_cesar.setObjectName("combo_csc_cesar")
        self.combo_csc_cesar.setStyleSheet("font-family: Courier")

        self.label_csc_scytale = QtWidgets.QLabel(parent=self.tab_csc)
        self.label_csc_scytale.setGeometry(QtCore.QRect(x1, 180, 47, 30))
        self.label_csc_scytale.setObjectName("label_csc_scytale")       
        self.combo_csc_scytale = QtWidgets.QComboBox(parent=self.tab_csc)
        self.combo_csc_scytale.setGeometry(QtCore.QRect(x2, 180, 300, 22))
        self.combo_csc_scytale.setObjectName("combo_csc_scytale")
        self.combo_csc_scytale.setStyleSheet("font-family: Courier")

        #self.spinbox_csc_scytale = QtWidgets.QSpinBox(parent=self.tab_csc)        
        #self.spinbox_csc_scytale.setObjectName("spinbox_csc_scytale")
        #self.spinbox_csc_scytale.setGeometry(QtCore.QRect(x1 + 60, 40, 40, 20))
        #self.spinbox_csc_scytale.setStyleSheet("background-color: salmon")
        #self.spinbox_csc_scytale.setRange(2, 100)
        #self.spinbox_csc_scytale.setValue(2)
        

        # onglet comptage texte
        self.tab_ctx = QtWidgets.QWidget()
        self.tab_ctx.setObjectName("tab_ctx")

        self.label_ctx_text1 = QtWidgets.QLabel(parent=self.tab_ctx)
        self.label_ctx_text1.setGeometry(QtCore.QRect(x1, 20, 100, 20))
        self.label_ctx_text1.setObjectName("label_ctx_texte1")
        self.label_ctx_text1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)        
        
        self.textedit_ctx_text1 = QtWidgets.QTextEdit(parent=self.tab_ctx)
        self.textedit_ctx_text1.setGeometry(QtCore.QRect(x1, 45, 450, 200))
        self.textedit_ctx_text1.setObjectName("text_ctx_text1")
        self.textedit_ctx_text1.setStyleSheet("font-family: Courier")
        
        self.label_ctx_crypto = QtWidgets.QLabel(parent=self.tab_ctx)
        self.label_ctx_crypto.setGeometry(QtCore.QRect(x1, 255, 105, 50))
        self.label_ctx_crypto.setObjectName("label_ctx_crypto")
        self.label_ctx_crypto.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_ctx_crypto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.combo_ctx_crypto = QtWidgets.QComboBox(parent=self.tab_ctx)
        self.combo_ctx_crypto.setGeometry(QtCore.QRect(x2 - 20, 255, 310, 22))
        self.combo_ctx_crypto.setObjectName("combo_ctx_crypto")
        self.combo_ctx_crypto.setStyleSheet("font-family: Courier")
        self.combo_ctx_crypto.setEditable(True)
        
        self.pushButton_ctx_Go = QtWidgets.QPushButton(parent=self.tab_ctx)
        self.pushButton_ctx_Go.setGeometry(QtCore.QRect(350, 290, 75, 45))
        self.pushButton_ctx_Go.setObjectName("pushButton_ctx_Go")
        self.pushButton_ctx_Go.setStyleSheet("background-color: dodgerblue")



        self.label_ctx_unitaires = QtWidgets.QLabel(parent=self.tab_ctx)
        self.label_ctx_unitaires.setGeometry(QtCore.QRect(x6, 20, 120, 25))
        self.label_ctx_unitaires.setObjectName("label_ctx_unitaires")
        self.label_ctx_unitaires.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        
        
        self.label_ctx_direc_df = QtWidgets.QLabel(parent=self.tab_ctx)
        self.label_ctx_direc_df.setGeometry(QtCore.QRect(x4, 50, 98, 35))
        self.label_ctx_direc_df.setObjectName("label_ctx_direc_df")
        self.label_ctx_direc_df.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_ctx_direc_df.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        
        self.combo_ctx_direc_df = QtWidgets.QComboBox(parent=self.tab_ctx)
        self.combo_ctx_direc_df.setGeometry(QtCore.QRect(x5, 55, 400, 22))
        self.combo_ctx_direc_df.setObjectName("combo_ctx_direc_df")
        self.combo_ctx_direc_df.setStyleSheet("font-family: Courier")

        self.label_ctx_direc_ench = QtWidgets.QLabel(parent=self.tab_ctx)
        self.label_ctx_direc_ench.setGeometry(QtCore.QRect(x4, 90, 98, 35))
        self.label_ctx_direc_ench.setObjectName("label_ctx_direc_ench")
        self.label_ctx_direc_ench.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_ctx_direc_ench.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        
        self.combo_ctx_direc_ench = QtWidgets.QComboBox(parent=self.tab_ctx)
        self.combo_ctx_direc_ench.setGeometry(QtCore.QRect(x5, 95, 400, 22))
        self.combo_ctx_direc_ench.setObjectName("combo_ctx_direc_ench")
        self.combo_ctx_direc_ench.setStyleSheet("font-family: Courier")
        
        self.label_ctx_inverse_fd = QtWidgets.QLabel(parent=self.tab_ctx)
        self.label_ctx_inverse_fd.setGeometry(QtCore.QRect(x4, 125, 98, 35))
        self.label_ctx_inverse_fd.setObjectName("label_ctx_inverse_fd")
        self.label_ctx_inverse_fd.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_ctx_inverse_fd.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        
        self.combo_ctx_inverse_fd = QtWidgets.QComboBox(parent=self.tab_ctx)
        self.combo_ctx_inverse_fd.setGeometry(QtCore.QRect(x5, 130, 400, 22))
        self.combo_ctx_inverse_fd.setObjectName("combo_ctx_inverse_fd")
        self.combo_ctx_inverse_fd.setStyleSheet("font-family: Courier")
        

        self.label_ctx_couples = QtWidgets.QLabel(parent=self.tab_ctx)
        self.label_ctx_couples.setGeometry(QtCore.QRect(x6, y2, 120, 25))
        self.label_ctx_couples.setObjectName("label_ctx_couples")
        self.label_ctx_couples.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        
        self.label_ctx_direc_ll = QtWidgets.QLabel(parent=self.tab_ctx)
        self.label_ctx_direc_ll.setGeometry(QtCore.QRect(x4 + 35, y2 + 30, 63, 35))
        self.label_ctx_direc_ll.setObjectName("label_ctx_direc_ll")
        self.label_ctx_direc_ll.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_ctx_direc_ll.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        
        self.combo_ctx_direc_ll = QtWidgets.QComboBox(parent=self.tab_ctx)
        self.combo_ctx_direc_ll.setGeometry(QtCore.QRect(x5, y2 + 35, 400, 22))
        self.combo_ctx_direc_ll.setObjectName("combo_ctx_direc_ll")
        self.combo_ctx_direc_ll.setStyleSheet("font-family: Courier")

        self.label_ctx_inverse_ll = QtWidgets.QLabel(parent=self.tab_ctx)
        self.label_ctx_inverse_ll.setGeometry(QtCore.QRect(x4 + 35, y2 + 70, 63, 35))
        self.label_ctx_inverse_ll.setObjectName("label_ctx_inverse_ll")
        self.label_ctx_inverse_ll.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_ctx_inverse_ll.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        
        self.combo_ctx_inverse_ll = QtWidgets.QComboBox(parent=self.tab_ctx)
        self.combo_ctx_inverse_ll.setGeometry(QtCore.QRect(x5, y2 + 75, 400, 22))
        self.combo_ctx_inverse_ll.setObjectName("combo_ctx_inverse_ll")
        self.combo_ctx_inverse_ll.setStyleSheet("font-family: Courier")
        
        
        # onglet cryptanalyse
        self.tab_can = QtWidgets.QWidget()
        self.tab_can.setObjectName("tab_can")


        self.label_can_alpha = QtWidgets.QLabel(parent=self.tab_can)
        self.label_can_alpha.setGeometry(QtCore.QRect(x1, 20, 47, 20))
        self.label_can_alpha.setObjectName("label_can_alpha")

        self.lineEdit_can_alpha = QtWidgets.QLineEdit(parent=self.tab_can)
        self.lineEdit_can_alpha.setGeometry(QtCore.QRect(x2, 20, 200, 20))
        self.lineEdit_can_alpha.setObjectName("lineEdit_can_alpha")
        self.lineEdit_can_alpha.setStyleSheet("font-family: Courier")

        self.label_can_crypto = QtWidgets.QLabel(parent=self.tab_can)
        self.label_can_crypto.setGeometry(QtCore.QRect(x1, 40, 47, 20))
        self.label_can_crypto.setObjectName("label_can_crypto")
        
        self.textedit_can_crypto = QtWidgets.QTextEdit(parent=self.tab_can)
        self.textedit_can_crypto.setGeometry(QtCore.QRect(x1, 65, 400, 200))
        self.textedit_can_crypto.setObjectName("text_can_crypto")
        self.textedit_can_crypto.setStyleSheet("font-family: Courier")

        self.pushButton_can_Go = QtWidgets.QPushButton(parent=self.tab_can)
        self.pushButton_can_Go.setGeometry(QtCore.QRect(330, 270, 75, 45))
        self.pushButton_can_Go.setObjectName("pushButton_can_Go")
        self.pushButton_can_Go.setStyleSheet("background-color: dodgerblue")

        self.label_can_analyse = QtWidgets.QLabel(parent=self.tab_can)
        self.label_can_analyse.setGeometry(QtCore.QRect(x1, 320, 50, 20))
        self.label_can_analyse.setObjectName("label_can_analyse")
        
        self.textedit_can_analyse = QtWidgets.QTextEdit(parent=self.tab_can)
        self.textedit_can_analyse.setGeometry(QtCore.QRect(x1, 345, 400, 100))
        self.textedit_can_analyse.setObjectName("text_can_analyse")
        self.textedit_can_analyse.setStyleSheet("font-family: Courier")
        self.textedit_can_analyse.setReadOnly(True)
        
        self.window_can_graph = Window_Graph(parent = self.tab_can)
        self.window_can_graph.setGeometry(QtCore.QRect(x1, 460, 1100, 250))

        self.label_can_decrypte = QtWidgets.QLabel(parent=self.tab_can)
        self.label_can_decrypte.setGeometry(QtCore.QRect(x4, 40, 90, 20))
        self.label_can_decrypte.setObjectName("label_can_decrypte")
        
        self.textedit_can_decrypte = QtWidgets.QTextEdit(parent=self.tab_can)
        self.textedit_can_decrypte.setGeometry(QtCore.QRect(x4, 65, 400, 200))
        self.textedit_can_decrypte.setObjectName("text_can_decrypte")
        self.textedit_can_decrypte.setStyleSheet("font-family: Courier")
        self.textedit_can_decrypte.setReadOnly(True)

        self.pushButton_can_force_longcle = QtWidgets.QPushButton(parent=self.tab_can)
        self.pushButton_can_force_longcle.setGeometry(QtCore.QRect(x4 + 255, 25, 95, 35))
        self.pushButton_can_force_longcle.setObjectName("pushButton_can_force_longcle")
        self.pushButton_can_force_longcle.setStyleSheet("background-color: dodgerblue")

        self.spinbox_can_force_longcle = QtWidgets.QSpinBox(parent=self.tab_can)        
        self.spinbox_can_force_longcle.setObjectName("spinbox_can_force_longcle")
        self.spinbox_can_force_longcle.setGeometry(QtCore.QRect(x4 + 360, 40, 40, 20))
        self.spinbox_can_force_longcle.setStyleSheet("background-color: lightblue")

        self.label_can_vige = QtWidgets.QLabel(parent=self.tab_can)
        self.label_can_vige.setGeometry(QtCore.QRect(x4, y2 - 20, 115, 20))
        self.label_can_vige.setObjectName("label_can_vige")

        self.combo_can_vige = QtWidgets.QComboBox(parent=self.tab_can)
        self.combo_can_vige.setGeometry(QtCore.QRect(x4, y2, 400, 22))
        self.combo_can_vige.setObjectName("combo_can_vige")
        self.combo_can_vige.setStyleSheet("font-family: Courier")

        self.combo_can_vige_freq = QtWidgets.QComboBox(parent=self.tab_can)
        self.combo_can_vige_freq.setGeometry(QtCore.QRect(x4, y2+40, 400, 22))
        self.combo_can_vige_freq.setObjectName("combo_can_vige_freq")
        self.combo_can_vige_freq.setStyleSheet("font-family: Courier")
        self.combo_can_vige_freq.setVisible(False)

        self.combo_can_valeurs = QtWidgets.QComboBox(parent=self.tab_can)
        self.combo_can_valeurs.setGeometry(QtCore.QRect(x4, y2+60, 400, 22))
        self.combo_can_valeurs.setObjectName("combo_can_valeurs")
        self.combo_can_valeurs.setStyleSheet("font-family: Courier")
        self.combo_can_valeurs.setVisible(False)
  
        # Ajout des onglets à la tab d'onglets
        self.tabWidget.addTab(self.tab_cc, "")        
        self.tabWidget.addTab(self.tab_csc, "")
        self.tabWidget.addTab(self.tab_ctx, "")
        self.tabWidget.addTab(self.tab_can, "")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(parent=self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    #def eventFilter(self, source, event):
    #    if event.type() == QtCore.QEvent.ContextMenu and source is self.combo_cc_crypto:
    #        menu = QMenu()
    #        menu.addAction('Action 1')
    #        menu.addAction('Action 2')
    #        menu.addAction('Action 3')
    #
    #        if menu.exec_(event.globalPos()):
    #            item = source.itemAt(event.pos())
    #            print(item.text())
    #        return True
    #    return super().eventFilter(source, event)

    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dkrypton MM"))
        
        self.label_cc_alpha.setText(_translate("MainWindow", "Alphabet"))
        self.lineEdit_cc_alpha.setText(_translate("MainWindow", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.label_cc_alphaw.setText(_translate("MainWindow", "Alphabet w"))
        self.lineEdit_cc_alphaw.setText(_translate("MainWindow", "ABCDEFGHIJKLMNOPQRSTUVXYZ"))
        self.label_cc_crypto.setText(_translate("MainWindow", "Crypto"))
        self.label_cc_cle1.setText(_translate("MainWindow", "Clé 1"))
        self.label_cc_cle2.setText(_translate("MainWindow", "Clé 2"))
        self.label_cc_cle3.setText(_translate("MainWindow", "Clé 3"))
        self.label_cc_cle4.setText(_translate("MainWindow", "Clé 4"))
        self.pushButton_cc_Go.setText(_translate("MainWindow", "Go !"))
        
        self.label_cc_vigenere.setText(_translate("MainWindow", "Vigenère\nCrypto - C1"))
        self.label_cc_cryptoplus.setText(_translate("MainWindow", "Crypto + Clé"))
        self.label_cc_cryptomoins.setText(_translate("MainWindow", "Crypto - Clé"))
        self.label_cc_beaufortall.setText(_translate("MainWindow", "Beaufort Allemand\nCrypto + Clé"))
        self.label_cc_beaufort.setText(_translate("MainWindow", "Beaufort\nC1 - Crypto"))

        self.label_csc_alpha.setText(_translate("MainWindow", "Alphabet"))
        self.lineEdit_csc_alpha.setText(_translate("MainWindow", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.label_csc_alphaw.setText(_translate("MainWindow", "Alphabet w"))
        self.lineEdit_csc_alphaw.setText(_translate("MainWindow", "ABCDEFGHIJKLMNOPQRSTUVXYZ"))
        self.label_csc_crypto.setText(_translate("MainWindow", "Crypto"))
        self.pushButton_csc_Go.setText(_translate("MainWindow", "Go !"))
        self.label_csc_cesar.setText(_translate("MainWindow", "César"))
        self.label_csc_scytale.setText(_translate("MainWindow", "Scytale\n1 lettre sur N"))

                
        self.label_ctx_text1.setText(_translate("MainWindow", "Texte où compter"))
        self.label_ctx_crypto.setText(_translate("MainWindow", "CRYPTO\n(Clé de comptage)\nséparateur ."))
        self.pushButton_ctx_Go.setText(_translate("MainWindow", "Go !"))
        self.label_ctx_unitaires.setText(_translate('MainWindow', "Comptages unitaires"))
        self.label_ctx_direc_df.setText(_translate("MainWindow", "direct\ndébut texte -> fin"))
        self.label_ctx_direc_ench.setText(_translate("MainWindow", "direct, enchaîné"))
        self.label_ctx_inverse_fd.setText(_translate("MainWindow", "inversé\nfin texte -> début"))

        self.label_ctx_couples.setText(_translate('MainWindow', "Comptages couples"))
        self.label_ctx_direc_ll.setText(_translate("MainWindow", "direct\nligne, lettre"))
        self.label_ctx_inverse_ll.setText(_translate("MainWindow", "inversé\nlettre, ligne"))

        self.label_can_alpha.setText(_translate("MainWindow", "Alphabet"))
        self.lineEdit_can_alpha.setText(_translate("MainWindow", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.pushButton_can_Go.setText(_translate("MainWindow", "Analyse\nFréquences"))
        self.label_can_crypto.setText(_translate("MainWindow", "Crypto"))
        self.label_can_analyse.setText(_translate("MainWindow", "Analyse :"))
        self.label_can_decrypte.setText(_translate("MainWindow", "Texte décrypté"))
        self.pushButton_can_force_longcle.setText(_translate("MainWindow", "Forcer avec la\nlongueur de clé :"))
        self.label_can_vige.setText(_translate("MainWindow", "Décryptages possibles :"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cc), _translate("MainWindow", "Crypto Classiques"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_csc), _translate("MainWindow", "Crypto sans clé"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_can), _translate("MainWindow", "Cryptanalyse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ctx), _translate("MainWindow", "Comptage texte"))
        
        
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
