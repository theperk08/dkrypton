# controller.py

from functools import partial
from PyQt6.QtWidgets import QMenu
from dkrypton.fonctions import *
                             

class DkryptonCtrl():
    
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view        
        self._connectSignals()  # Register signals/slots
        print('ici')
    
    def _ccDecode(self, rien):
        """
        lance tous les décodages de l'onglet Crypto Classiques
        """

        # on récupère tous les éléments utiles de l'onglet, sous forme de dico
        dico_elements = self._view.dico_cc()
        print(dico_elements)
        
        #Commence par effacer les anciens décodages éventuels
        self._view.efface_cc()

        # décryptages
        
        result_vigenere = self._evaluate.vigenere_deco(dico_elements['crypto'],
                                              dico_elements['cle1'],
                                              dico_elements['alphabet'],
                                              0)
        
        
        print('le résulat du Vigenère est : ', result_vigenere)

        
        result_beaufort_all = self._evaluate.vigenere_deco(dico_elements['crypto'],
                                              dico_elements['cle1'],
                                              dico_elements['alphabet'],
                                              1)
        
        
        print('le résulat du Beaufort Allemand est : ', result_beaufort_all)

        result_beaufort = self._evaluate.vigenere_deco(dico_elements['crypto'],
                                              dico_elements['cle1'],                                            
                                              dico_elements['alphabet'],
                                              2)

        print('le résulat du Beaufort est : ', result_beaufort)
        
        
        result_crypto_plus = self._evaluate.crypto_plus(self._view._ui.combo_cc_crypto.currentText(),
                                              self._evaluate.transfo_alpha_num(dico_elements['cle1'],
                                                                               dico_elements['alphabet']),
                                              dico_elements['alphabet'],
                                            True) #pour addition
        
        
        print("le résulat du Crypto_plus est : ", result_crypto_plus)

        result_crypto_moins = self._evaluate.crypto_plus(dico_elements['crypto'],
                                              self._evaluate.transfo_alpha_num(dico_elements['cle1'],
                                                                               dico_elements['alphabet']),
                                              dico_elements['alphabet'],
                                            False) #pour soustraction
       
        
        print("le résulat du Crypto_moins est : ", result_crypto_moins)

        # AFFICHAGE FINAL

        affichages = {'vigenere' : result_vigenere,
                      'beaufort_allemand' : result_beaufort_all,
                      'beaufort' : result_beaufort,
                      'crypto_plus' : result_crypto_plus,
                      'crypto_moins' : result_crypto_moins
                      }
        
        self._view.affiche_cc(affichages)

    def _cscDecode(self, rien):
        """
        lance tous les décodages de l'onglet Crypto Sans Clé
        """
        # on récupère tous les éléments utiles de l'onglet, sous forme de dico
        dico_elements = self._view.dico_csc()
        print(dico_elements)
        
        #Commence par effacer les anciens décodages éventuels
        self._view.efface_csc()

        # décryptages    

        ## les 25 décalages possible d'un César
        liste_cesar = []
        for i in range(1, 26):
            result = self._evaluate.crypto_plus(dico_elements['crypto'],
                                                [i],
                                                dico_elements['alphabet'],
                                                True) #pour addition
            liste_cesar += [result]

        ## les décryptages de Scytale
        liste_scytale = []
        crypto = dico_elements['crypto']
        for i in range(2, len(crypto) + 1):
            result = crypto[0]
            num = 0
            for k in range(len(crypto) - 1):
                num += i
                result += crypto[num % len(crypto)]
            liste_scytale += [result]

        affichages = {"cesar" : liste_cesar,
                      "scytale" : liste_scytale}
        
        self._view.affiche_csc(affichages)
           
    def _ctxDecode(self, rien):
        """
        lance tous les décodages de l'onglet Crypto Sans Clé
        """      
        # on récupère tous les éléments utiles de l'onglet, sous forme de dico
        dico_elements = self._view.dico_ctx()
        print(dico_elements)
        
        #;Commence par effacer les anciens décodages éventuels        
        self._view.efface_ctx()

        # Décryptages
        
        # stockage du crypto en liste
        liste_crypto = list(map(int,dico_elements['crypto'].split('.')))
       

        # récupération du texte
        texte = dico_elements['texte']
        # par lignes pour comptages couplés
        text_lignes = str(texte).splitlines()
        # et tout à la suite pour comptages unitaires
        text_tout = ''.join(text_lignes)
        
        # comptages unitaires
        ## direct début fin
        result_ddf = ""
        for nombre in liste_crypto:
            try:
                result_ddf += text_tout[nombre - 1]
            except:
                result_ddf += '?'

        ## direct enchaîné
        result_de = ""
        numero = 0
        for nombre in liste_crypto:
            try:
                numero += nombre 
                result_de += text_tout[numero - 1]
            except:
                result_de += '?'

        ## inverse fin début
        result_ifd = ""
        for nombre in liste_crypto:
            try:
                result_ifd += text_tout[-nombre]
            except:
                result_ifd += '?'

        # comptages couplés (seulement si nombre pairs de nombres dans le crypto

        result_dll = ""
        result_ill = ""
        if len(liste_crypto) % 2 == 0:
            ## direct ligne lettre
            
            for k in range(len(liste_crypto)//2):
              
                try:
                    result_dll += text_lignes[liste_crypto[2*k] - 1][liste_crypto[2*k + 1] - 1]
                except:
                    result_dll += '?'
            ## inversé lettre ligne
            
            for k in range(len(liste_crypto)//2):              
                try:
                    result_ill += text_lignes[liste_crypto[2*k + 1] - 1][liste_crypto[2*k] - 1]
                except:
                    result_ill += '?'
        

        affichages = {'result_ddf' : result_ddf,
                      'result_de' : result_de,
                      'result_ifd' : result_ifd,
                      'result_dll' : result_dll,
                      'result_ill' : result_ill}

        self._view.affiche_ctx(affichages)

    
    
    def _canDecode(self):
        """
        lance tous les décodages de l'onglet Crypto Sans Clé
        """

        # on récupère tous les éléments utiles de l'onglet, sous forme de dico
        dico_elements = self._view.dico_can()

        print(dico_elements)
        #Commence par effacer les anciens décodages éventuels
        self._view.efface_can()
       
        # FORMATAGE DU TEXTE

        ### suppression des caractères de saut de lignes, de tabulation et d'espaces et autres non autorisés

    
        texte = dico_elements['crypto']

        texte_format = format_texte(texte)       


        ## création dico {lettres: nombre d'apparition}
        total = len(texte_format)
        dico_lettre = {}
        #alphabet = self._view._ui.lineEdit_can_alpha.text()
        alphabet = dico_elements['alphabet']
        print(alphabet)



        dico_lettre = compteLettres(texte_format, alphabet) 

        analyse = "Longueur du crypto : {}".format(total)

        ## dico {lettres : fréquences d'apparition}
        
        dico_freq = {key : value / total for key, value in dico_lettre.items()}
        print(dico_freq)

        ## Calcul IC

        IC = self._evaluate.calcul_IC(dico_lettre, total)        
        print(IC)
        
        
        analyse += '\nIC : ' + str(round(IC,6))        

      
 
        ## Affichage stats fréquences lettres    

        valeurs_x = list(dico_freq.keys())
        valeurs_y = list(dico_freq.values())

        print(valeurs_x, '\n', valeurs_y)

        freq_france = [0.0815, 0.0097, 0.0315, 0.0373, 0.1739, 0.0112, 0.0097, 0.0085, 0.0731, 0.045, 0.0002, 0.0569, 0.0287,
                       0.0712, 0.0528, 0.028, 0.0121, 0.0664, 0.0814, 0.0722, 0.0638, 0.0164, 0.0003, 0.0041, 0.0028, 0.0015]
        

        
        

        longueurs, cles_vigenere = self._evaluate.casse_vigenere(texte_format, [])


        analyse += '\n Longueur de clé : Clé probable'
        #analyse += '\n\nLongueur(s) probable(s) de clé si Vigenère : ' + ' ; '.join(longueurs)

        texte_decrypte = ''

        if len(longueurs) > 0:
            liste_texte = []
            for k in range(len(cles_vigenere)):
                cle_probable = self._evaluate.crypto_plus(cles_vigenere[k],
                                                      [4], # car lettre la plus fréquente est E
                                                      dico_elements['alphabet'],
                                                      False)
                analyse += '\n{0:16} : {1}'.format(longueurs[k], cle_probable)

                texte_decrypte = self._evaluate.vigenere_deco(dico_elements['crypto'],
                                                              cle_probable,
                                                              dico_elements['alphabet'],
                                                              0)
                liste_texte += [texte_decrypte]

        # dico de freqences du texte decrypte avec chacune des cles
        freq_decrypte = []
        for textes in liste_texte:
            text_format = format_texte(textes)
            dico_lettre = compteLettres(text_format, alphabet)
            dico_freq = {key : value / total for key, value in dico_lettre.items()}
            valeurs_y2 = list(dico_freq.values())
            freq_decrypte += [valeurs_y2]
            

        
        print(freq_decrypte)
            

        # AFFICHAGE FINAL DANS LA CASE Analyse:


        #dico_elements['analyse'].setText(analyse)      
        #self._view._ui.textedit_can_decrypte.setText(texte_decrypte)

        affichages = {'analyse' : analyse, 'decrypte' : liste_texte, 'freq' : freq_decrypte, 'valeurs' : [valeurs_x, valeurs_y, freq_france]}
        self._view.affiche_can(affichages)
        ## et graphique des stats de distrib des frequences
        self._view._ui.window_can_graph.plot(valeurs_x, valeurs_y, freq_france, freq_decrypte[0])

        

        

    def _canForce(self):        

        # on récupère tous les éléments utiles de l'onglet, sous forme de dico
        dico_elements = self._view.dico_can()

        print(dico_elements)
        #Commence par effacer les anciens décodages éventuels
        self._view.efface_can()
        

        analyse = "Avec la longueur {} suggérée, ".format(dico_elements['long_cle'].value())

        # on récupère la longueur de la clé souhaitée :
        texte = dico_elements['crypto']
        texte_format = format_texte(texte)      
             
        

        longueur, cle_vigenere = self._evaluate.casse_vigenere(texte_format, [dico_elements['long_cle'].value()])

        
        cle_probable = self._evaluate.crypto_plus(cle_vigenere[0],
                                                  [4], # car lettre la plus fréquente est E
                                                  dico_elements['alphabet'],
                                                  False)
        analyse += "Pour une longueur de {}, la clé probable est {}\n".format(longueur[0], cle_probable)
        

        texte_decrypte = self._evaluate.vigenere_deco(dico_elements['crypto'],
                                                      cle_probable,
                                                      dico_elements['alphabet'],
                                                      0)

        affichages = {'analyse' : analyse, 'decrypte' : [texte_decrypte]}
        self._view.affiche_can(affichages)

    def _canIndexChanged(self, index):
        self._view._ui.textedit_can_decrypte.setText(self._view._ui.combo_can_vige.itemText(index))
        liste_x = [x.strip()[1] for x in self._view._ui.combo_can_valeurs.itemText(0)[1:-1].split(',')]
        liste_y = [round(float(x),2) for x in self._view._ui.combo_can_valeurs.itemText(1)[1:-1].split(',')]
        liste_france = [round(float(x),2) for x in self._view._ui.combo_can_valeurs.itemText(2)[1:-1].split(',')]
        liste_z = [round(float(x),2) for x in self._view._ui.combo_can_vige_freq.itemText(index)[1:-1].split(',')]
        self._view._ui.window_can_graph.plot(liste_x,
                                             liste_y,
                                             liste_france,
                                             liste_z)

        
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
        
        self._view._ui.pushButton_cc_Go.clicked.connect(partial(self._ccDecode))
        self._view._ui.pushButton_csc_Go.clicked.connect(partial(self._cscDecode))
        self._view._ui.pushButton_ctx_Go.clicked.connect(partial(self._ctxDecode))
        self._view._ui.pushButton_can_Go.clicked.connect(partial(self._canDecode))
        self._view._ui.pushButton_can_force_longcle.clicked.connect(partial(self._canForce))
        self._view._ui.combo_can_vige.activated.connect(partial(self._canIndexChanged))
   
