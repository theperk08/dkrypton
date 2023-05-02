# view.py

# pyuic6 main_view.ui -o main_view.py

from PyQt6.QtCore import QSize, Qt, pyqtSlot
from PyQt6.QtWidgets import (QApplication, QGridLayout, QWidget, QMenu, QMainWindow, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton, QWidget,
QTabWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QAction


from dkrypton.view_dkrypton import Ui_MainWindow # MplCanvas

class DkryptonUi(QMainWindow):
    """
    Main calculator GUI
    """
    def __init__(self):
        super().__init__()
        
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)


    def dico_cc(self):
        dico = {'alphabet' : self._ui.lineEdit_cc_alpha.text(),
                'crypto' : self._ui.combo_cc_crypto.currentText(),
                'cle1' : self._ui.combo_cc_cle1.currentText()                
                }
        return dico

    def affiche_cc(self, affichages):
        self._ui.lineEdit_cc_vigenere.setText(affichages['vigenere'])
        self._ui.lineEdit_cc_beaufortall.setText(affichages['beaufort_allemand'])
        self._ui.lineEdit_cc_beaufort.setText(affichages['beaufort'])
        self._ui.combo_cc_cryptoplus.addItem(affichages['crypto_plus'])
        self._ui.combo_cc_cryptomoins.addItem(affichages['crypto_moins'])            
    
    def efface_cc(self):
        self._ui.combo_cc_cryptoplus.clear()
        self._ui.combo_cc_cryptomoins.clear()
        self._ui.lineEdit_cc_vigenere.setText("")
        self._ui.lineEdit_cc_beaufortall.setText("")
        self._ui.lineEdit_cc_beaufort.setText("")


    def dico_csc(self):
        dico = {'alphabet' : self._ui.lineEdit_csc_alpha.text(),
                'crypto' : self._ui.combo_csc_crypto.currentText()              
                }
        return dico

    def affiche_csc(self, affichages):
        for result_cesar in affichages['cesar']:
            self._ui.combo_csc_cesar.addItem(result_cesar)

        for result_scytale in affichages['scytale']:
            self._ui.combo_csc_scytale.addItem(result_scytale)
            
    def efface_csc(self):
        self._ui.combo_csc_cesar.clear()
        self._ui.combo_csc_scytale.clear()


    def dico_ctx(self):
        dico = {'texte' : self._ui.textedit_ctx_text1.toPlainText(),
                'crypto' : self._ui.combo_ctx_crypto.currentText()                               
                }
        return dico

    def affiche_ctx(self, affichages):
        self._ui.combo_ctx_direc_df.addItem(affichages['result_ddf'])
        self._ui.combo_ctx_direc_ench.addItem(affichages['result_de'])
        self._ui.combo_ctx_inverse_fd.addItem(affichages['result_ifd'])
        self._ui.combo_ctx_direc_ll.addItem(affichages['result_dll']) 
        self._ui.combo_ctx_inverse_ll.addItem(affichages['result_ill'])
        
    
    def efface_ctx(self):
        self._ui.combo_ctx_direc_df.clear()
        self._ui.combo_ctx_direc_ench.clear()
        self._ui.combo_ctx_inverse_fd.clear()
        
        self._ui.combo_ctx_direc_ll.clear()
        self._ui.combo_ctx_inverse_ll.clear()
        


    def dico_can(self):
        dico = {'alphabet' : self._ui.lineEdit_can_alpha.text(),
                'crypto' : self._ui.textedit_can_crypto.toPlainText(),
                'analyse' : self._ui.textedit_can_analyse,
                'long_cle' : self._ui.spinbox_can_force_longcle
                }
        return dico

    def affiche_can(self, affichages):
        self._ui.textedit_can_analyse.setText(affichages['analyse'])
        for k in range(len(affichages['decrypte'])):
            self._ui.combo_can_vige.addItem(affichages['decrypte'][k])
            
        self._ui.textedit_can_decrypte.setText(affichages['decrypte'][0])        
    
    def efface_can(self):
        self._ui.textedit_can_analyse.setText('')
        self._ui.textedit_can_decrypte.setText('')
        self._ui.combo_can_vige.clear()
 

        
    def contextMenuEvent(self, event):
        # Show the context menu
        self.context_menu.exec(event.globalPos())
 
       
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
        
    
    def cles1_remplacer(self):
        pass

    def cles2_remplacer(self):
        pass
    
    def cles1_ajouter(self):
        pass
    
    def cles2_ajouter(self):
        pass

    
