# controller.py

from functools import partial
import plotly.express as px

from PyQt6.QtWidgets import QMenu
                             

class DkryptonCtrl():
    """
    Main calculator controller class
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

        #on commence par effacer les éventuels anciens décodages
        self._view._ui.combo_cc_cryptoplus.clear()
        self._view._ui.combo_cc_cryptomoins.clear()
        self._view._ui.lineEdit_cc_vigenere.setText("")
        self._view._ui.lineEdit_cc_beaufortall.setText("")
        self._view._ui.lineEdit_cc_beaufort.setText("")
        
        result = self._evaluate.vigenere_deco(self._view._ui.combo_cc_crypto.currentText(),
                                              self._view._ui.combo_cc_cle1.currentText(),
                                              self._view._ui.lineEdit_cc_alpha.text(),
                                              0)
        
        self._view._ui.lineEdit_cc_vigenere.setText(result)
        print('le résulat du Vigenère est : ', result)

        
        result = self._evaluate.vigenere_deco(self._view._ui.combo_cc_crypto.currentText(),
                                              self._view._ui.combo_cc_cle1.currentText(),
                                              self._view._ui.lineEdit_cc_alpha.text(),
                                              1)
        
        self._view._ui.lineEdit_cc_beaufortall.setText(result)
        print('le résulat du Beaufort Allemand est : ', result)

        result = self._evaluate.vigenere_deco(self._view._ui.combo_cc_crypto.currentText(),
                                              self._view._ui.combo_cc_cle1.currentText(),                                            
                                              self._view._ui.lineEdit_cc_alpha.text(),
                                              2)
        
        self._view._ui.lineEdit_cc_beaufort.setText(result)
        print('le résulat du Beaufort est : ', result)
        
        
        result = self._evaluate.crypto_plus(self._view._ui.combo_cc_crypto.currentText(),
                                              self._evaluate.transfo_alpha_num(self._view._ui.combo_cc_cle1.currentText(),
                                                                               self._view._ui.lineEdit_cc_alpha.text()),
                                              self._view._ui.lineEdit_cc_alpha.text(),
                                            True) #pour addition
        self._view._ui.combo_cc_cryptoplus.addItem(result)
        
        print("le résulat du Crypto_plus est : ", result)

        result = self._evaluate.crypto_plus(self._view._ui.combo_cc_crypto.currentText(),
                                              self._evaluate.transfo_alpha_num(self._view._ui.combo_cc_cle1.currentText(),
                                                                               self._view._ui.lineEdit_cc_alpha.text()),
                                              self._view._ui.lineEdit_cc_alpha.text(),
                                            False) #pour soustraction
        self._view._ui.combo_cc_cryptomoins.addItem(result)
        
        print("le résulat du Crypto_moins est : ", result)

    def _cscDecode(self, rien):
        """
        lance tous les décodages de l'onglet Crypto Sans Clé
        """

        #Commence par effacer les anciens décodages éventuels
        self._view._ui.combo_csc_cesar.clear()

        # les 25 décalages possible d'un César
        for i in range(1, 26):
            result = self._evaluate.crypto_plus(self._view._ui.combo_csc_crypto.currentText(),
                                                [i],
                                                self._view._ui.lineEdit_cc_alpha.text(),
                                                True) #pour addition
            self._view._ui.combo_csc_cesar.addItem(result)
    
    def _ctxDecode(self, rien):
        """
        lance tous les décodages de l'onglet Crypto Sans Clé
        """
        print('ok')
        #Commence par effacer les anciens décodages éventuels
        
        self._view._ui.combo_ctx_direc_df.clear()
        self._view._ui.combo_ctx_direc_ll.clear()

        # stockage du crypto en liste
        liste_crypto = list(map(int,self._view._ui.combo_ctx_crypto.currentText().split('.')))

       

        # récupération du texte
        texte = self._view._ui.textedit_ctx_text1.toPlainText()
        # par lignes pour comptages couplés
        text_lignes = str(texte).splitlines()
        # et tout à la suite pour comptages unitaires
        text_tout = ''.join(text_lignes)
        
        # comptages unitaires
        result_ddf = ""
        for nombre in liste_crypto:
            try:
                result_ddf += text_tout[nombre - 1]
            except:
                result_ddf += '?'
            
        self._view._ui.combo_ctx_direc_df.addItem(result_ddf)

        # comptages couplés (seulement si nombre pairs de nombres dans le crypto
        if len(liste_crypto) % 2 == 0:
            result_dll = ""
            for k in range(len(liste_crypto)//2):
              
                try:
                    result_dll += text_lignes[liste_crypto[2*k] - 1][liste_crypto[2*k + 1] - 1]
                except:
                    result_dll += '?'
                
        

        self._view._ui.combo_ctx_direc_ll.addItem(result_dll)
        
    
    def _canDecode(self, rien):
        """
        lance tous les décodages de l'onglet Crypto Sans Clé
        """

        #Commence par effacer les anciens décodages éventuels
        #self._view._ui.combo_can_   .clear()


        # FORMATAGE DU TEXTE

        ### suppression des caractères de saut de lignes, de tabulation et d'espaces et autres non autorisés

        texte = self._view._ui.textedit_can_crypto.toPlainText()
        texte = str(texte).splitlines()
        texte = ''.join(texte)
        
        caract = ',.-_()[] \'"'
        
        for cara in caract:
            texte = texte.replace(cara,'')
            
        ### suppression des accentes et cédilles
        #accents = "âãàéèêëïîôôùüûÂÁÀÃÉÈËÊÎÏÔOÕõÙÜÛçÇÑñń"
        #equivalents = "aaaeeeeiioouuuAAAAEEEEIIOOOOUUUcCNnn"
        accents = "ÂÁÀÃÉÈËÊÎÏÔÕÙÜÛÇÑ"
        equivalents = "AAAAEEEEIIOOUUUCN"

        texte_format = texte.upper()
        for accent, lettre in zip(accents, equivalents):
            texte_format = texte_format.replace(accent, lettre)
        
        print(texte_format)


        ## création dico {lettres: nombre d'apparition}
        total = len(texte_format)
        dico = {}
        alphabet = self._view._ui.lineEdit_can_alpha.text()
        print(alphabet)
        
        for lettre in alphabet:
            dico[lettre] = 0
        for lettre in texte_format:
            try:
                dico[lettre] += 1
            except:
                pass
        

        print(dico) 

        analyse = "Longueur du crypto : {}".format(total)

        ## dico {lettres : fréquences d'apparition}
        
        dico_freq = {key : value / total for key, value in dico.items()}
        print(dico_freq)

        ## Calcul IC

        IC = self._evaluate.calcul_IC(dico, total)        
        print(IC)
        
        
        analyse += '\nIC : ' + str(round(IC,6))        

      
 
        ## Affichage stats fréquences lettres    

        valeurs_x = list(dico_freq.keys())
        valeurs_y = list(dico_freq.values())

        self._view._ui.window_can_graph.plot(valeurs_x, valeurs_y)

        longueur, cle_vigenere = self._evaluate.casse_vigenere(texte_format, '')


        analyse += '\n\nLongueur probable de clé si Vigenère : ' + str(longueur)
        cle_probable = self._evaluate.crypto_plus(cle_vigenere,
                                              [4], # car lettre la plus fréquente est E
                                              self._view._ui.lineEdit_can_alpha.text(),
                                              False)
        analyse += '\nClé probable : ' + cle_probable

        texte_decrypte = self._evaluate.vigenere_deco(texte_format,
                                                      cle_probable,
                                                      self._view._ui.lineEdit_can_alpha.text(),
                                                      0)

        # AFFICHAGE FINAL DANS LA CASE Analyse:
        self._view._ui.textedit_can_analyse.setText(analyse)

        
        self._view._ui.textedit_can_decrypte.setText(texte_decrypte)

        
    def _openMenu(self, location):
        # marche pas pour l'instant
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
        self._view._ui.pushButton_ctx_Go.clicked.connect(partial(self._ctxDecode, ''))
        self._view._ui.pushButton_can_Go.clicked.connect(partial(self._canDecode, ''))
   
