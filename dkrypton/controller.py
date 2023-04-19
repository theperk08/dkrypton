# controller.py

from functools import partial

from PyQt6.QtWidgets import QMenu
                             

class DkryptonCtrl():
    """
    Controller principal
    """
    
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()  # Register signals/slots
        print('ici')
    
    def _ccDecode(self, rien):
        """
        lance tous les décodages de l'onglet Crypto Classiques
        """

        # on commence par effacer les éventuels anciens décodages :
        self._view._ui.combo_cc_cryptoplus.clear()
        self._view._ui.combo_cc_cryptomoins.clear()
        self._view._ui.lineEdit_cc_vigenere.setText("")
        self._view._ui.lineEdit_cc_beaufortall.setText("")
        self._view._ui.lineEdit_cc_beaufort.setText("")
        
        # Vigenère
        result = self._evaluate.vigenere_deco(self._view._ui.combo_cc_crypto.currentText(),
                                              self._view._ui.combo_cc_cle1.currentText(),
                                              self._view._ui.lineEdit_cc_alpha.text(),
                                              0)
        
        self._view._ui.lineEdit_cc_vigenere.setText(result)        
        
        # Beaufort Allemand
        result = self._evaluate.vigenere_deco(self._view._ui.combo_cc_crypto.currentText(),
                                              self._view._ui.combo_cc_cle1.currentText(),
                                              self._view._ui.lineEdit_cc_alpha.text(),
                                              1)
        
        self._view._ui.lineEdit_cc_beaufortall.setText(result)
        
        # Beaufort
        result = self._evaluate.vigenere_deco(self._view._ui.combo_cc_crypto.currentText(),
                                              self._view._ui.combo_cc_cle1.currentText(),                                            
                                              self._view._ui.lineEdit_cc_alpha.text(),
                                              2)
        
        self._view._ui.lineEdit_cc_beaufort.setText(result)       
        
        # Crypto + Clé
        result = self._evaluate.crypto_plus(self._view._ui.combo_cc_crypto.currentText(),
                                              self._evaluate.transfo_alpha_num(self._view._ui.combo_cc_cle1.currentText(),
                                                                               self._view._ui.lineEdit_cc_alpha.text()),
                                              self._view._ui.lineEdit_cc_alpha.text(),
                                            True) #pour addition
        self._view._ui.combo_cc_cryptoplus.addItem(result)        
        
        # Crypto - Clé
        result = self._evaluate.crypto_plus(self._view._ui.combo_cc_crypto.currentText(),
                                              self._evaluate.transfo_alpha_num(self._view._ui.combo_cc_cle1.currentText(),
                                                                               self._view._ui.lineEdit_cc_alpha.text()),
                                              self._view._ui.lineEdit_cc_alpha.text(),
                                            False) #pour soustraction
        self._view._ui.combo_cc_cryptomoins.addItem(result)        
        

    def _cscDecode(self, rien):
        """
        lance tous les décodages de l'onglet Crypto Sans Clé
        """

        # Commence par effacer les anciens décodages éventuels
        self._view._ui.combo_csc_cesar.clear()

        # les 25 décalages possible d'un César
        for i in range(1, 26):
            result = self._evaluate.crypto_plus(self._view._ui.combo_csc_crypto.currentText(),
                                                [i],
                                                self._view._ui.lineEdit_cc_alpha.text(),
                                                True) #pour addition
            self._view._ui.combo_csc_cesar.addItem(result)
    
    # Création contextMenu : marche pas pour l'instant
    def _openMenu(self, location):
        menu = self.my_textbox.createStandardContextMenu()
        # add extra items to the menu
        print('ici bon')
        # show the menu
        menu.popup(self.mapToGlobal(location))

        
   
    def _connectSignals(self):
        """
        Associations des button clicks ("signals")
        et de leurs actions ("slots")        
        """
        
        self._view._ui.pushButton_cc_Go.clicked.connect(partial(self._ccDecode, ''))
        self._view._ui.pushButton_csc_Go.clicked.connect(partial(self._cscDecode, ''))
   
