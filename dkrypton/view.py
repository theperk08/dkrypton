# view.py

# pyuic6 main_view.ui -o main_view.py

from PyQt6.QtCore import QSize, Qt, pyqtSlot
from PyQt6.QtWidgets import (QApplication, QGridLayout, QWidget, QMenu, QMainWindow, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton, QWidget,
QTabWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QAction


from dkrypton.view_dkrypton import Ui_MainWindow

# Main view class for calculator GUI
class DkryptonUi(QMainWindow):
    """
    Main calculator GUI
    """
    def __init__(self):#, model): #, controller):
        super().__init__()
        #self.setWindowTitle("Dekrypton")
        #self.setFixedSize(1250, 850)

        #self._model = model
        #self._controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        #self._ui.pushButton_cc_Go.clicked.connect(self._controller._ccDecode)
         
    def contextMenuEvent(self, event):
        # Show the context menu
        self.context_menu.exec(event.globalPos())
 
    def action1_triggered(self):
        # Handle the "Action 1" action
        pass
 
    def action2_triggered(self):
        # Handle the "Action 2" action
        pass
 
    def action3_triggered(self):
        # Handle the "Action 3" action
        pass

    
    def faux_tab(self):
        self.faux = QWidget()
        self.faux_layout_v1 = QVBoxLayout()
        
        self._createDisplay()
        self._createButtons()

        self.faux.setLayout(self.faux_layout_v1)

        # en supprimant le return l'onglet n'apparaît pas
        #return self.faux

   
    def CreateMenuBar(self):  # pour créer le menu
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&Fichier", self)
        menuBar.addMenu(fileMenu)

        fichier_cryptos = QAction("Fichier de cryptos", self)
        
        fichier_cles1 = QMenu("Fichier de clés 1", self)
        cles1_remplacer = QAction("Remplacer par", self)
        fichier_cles1.addAction(cles1_remplacer)
        cles1_ajouter = QAction("Ajouter", self)
        fichier_cles1.addAction(cles1_ajouter)
        
        fichier_cles2 = QMenu("Fichier de clés 2", self)
        cles2_remplacer = QAction("Remplacer par", self)
        fichier_cles2.addAction(cles2_remplacer)
        cles2_ajouter = QAction("Ajouter", self)
        fichier_cles2.addAction(cles2_ajouter)
        

        quitter = QAction('Quitter', self)

        fileMenu.addAction(fichier_cryptos)
        fileMenu.addMenu(fichier_cles1)
        fileMenu.addMenu(fichier_cles2)
        fileMenu.addAction(quitter)

        # Creating menus using a title
        toolMenu = menuBar.addMenu("&Outils")
        reglages = QAction("Réglages", self)
        casser_playfair = QAction("Casser Playfair", self)
        
        toolMenu.addAction(reglages)
        toolMenu.addAction(casser_playfair)
        
        helpMenu = menuBar.addMenu("&Aide")
        apropos = QAction("À propos", self)
        aide = QAction("Aide", self)

        helpMenu.addAction(apropos)
        helpMenu.addAction(aide)
        
    
    def _createDisplay(self):
        """
        Calculator display/output
        """
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.faux_layout_v1.addWidget(self.display)
        
    def _createButtons(self):
        """
        Calculator buttons
        """
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text: position on QGridLayout
        buttons = {"7": (0, 0),
                   "8": (0, 1),
                   "9": (0, 2),
                   "/": (0, 3),
                   "C": (0, 4),
                   "4": (1, 0),
                   "5": (1, 1),
                   "6": (1, 2),
                   "*": (1, 3),
                   "(": (1, 4),
                   "1": (2, 0),
                   "2": (2, 1),
                   "3": (2, 2),
                   "-": (2, 3),
                   ")": (2, 4),
                   "0": (3, 0),
                   "00": (3, 1),
                   ".": (3, 2),
                   "+": (3, 3),
                   "=": (3, 4),
                  }
        # Create buttons and add to grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to cc_layout_v2 layout
        self.faux_layout_v1.addLayout(buttonsLayout)
        #self.cc_layout_v2.addLayout(buttonsLayout)
        
    def setDisplayText(self, text):
        """
        Set the text/content in calculator display
        """
        self.display.setText(text)
        self.display.setFocus()
        
    def displayText(self):
        """
        Get current text/content from calculator display
        """
        return self.display.text()
        
    def clearDisplay(self):
        """
        Clear calculator display
        """
        self.setDisplayText("")

    def cles1_remplacer(self):
        pass

    def cles2_remplacer(self):
        pass
    
    def cles1_ajouter(self):
        pass
    
    def cles2_ajouter(self):
        pass

    def clearDisplay_cc(self):
        """
        Clear calculator display
        """
        pass
