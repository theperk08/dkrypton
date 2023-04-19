# model.py

from dkrypton.constants import *

# Simple "model" to handle calculator functionality
# This function just uses the Python "eval()" function
# to evaluate the expression entered.


class Models:
    def __init__(self):
        pass

    
    def evaluateExpression(expression):
        """
        Evaluate expression in calculator display
        and return result.
        """
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = ERROR_MSG
            
        return result
    

    def is_num(chaine):
        """
        Vérifie si chaine est du style : 4.20.-5.6.0
        cad des nombres (entiers positifs ou négatifs)
        séparés par des points
        """       

        pass
    

    def is_alpha(chaine):
        """
        Vérifie que la chaîne n'est constituée que de caractètres alphabétiques classiques
        
        """
        ok = True       

        return ok
           

    def transfo_alpha_num(chaine, alpha):
        """
        permet de transformer une chaine alphanumérique (str) en liste de int
        en cherchant la position (index + 1) de la lettre de la chaine dans l'alpha
        """
        
        resultat = []
        try:
            for lettre in chaine:
                if alpha.lower().find(lettre.lower()) >= 0:
                    resultat += [alpha.lower().find(lettre.lower()) + 1]
                else:
                    resultat += [0]
                #print(resultat)
        except:
            print('problème')
        print('cle en num:', resultat)
        return resultat
    

    def transfo_num_alpha(chaine, alpha):
        """
        permet de transformer une liste de int en chaine alphanumérique (str)
        
        """
        return ""  

    def vigenere_deco(crypto, cle, alpha, add_beauf):
        """
        décryptage suivant Vigenere
        crypto, cle et alpha : sous forme alphabétique (str)
        les autres caractères restent inchangés
        add_beauf = 0 pour un Vigenere, 1 pour Beaufort Allemand, 2 pour un Beaufort
        """
        
        resultat = ""        
        k = 0
        
        for i, lettre in enumerate(crypto):            
            
            if alpha.lower().find(lettre.lower()) >= 0 and alpha.lower().find(cle.lower()[k % len(cle)]) >= 0:
                if add_beauf == 0:
                    lettre_deco =  alpha.lower().index(lettre.lower()) - alpha.lower().index(cle.lower()[k % len(cle)])
                if add_beauf == 1:
                    lettre_deco =  alpha.lower().index(lettre.lower()) + alpha.lower().index(cle.lower()[k % len(cle)])
                if add_beauf == 2:
                    lettre_deco =  alpha.lower().index(cle.lower()[k % len(cle)]) - alpha.lower().index(lettre.lower())
                lettre_deco %= 26
                if lettre.islower():
                    resultat += alpha.lower()[lettre_deco]
                else:
                    resultat += alpha.upper()[lettre_deco]
                k += 1
            else:
                resultat += lettre
            
        return resultat
    

    def crypto_plus(crypto, cle, alpha, addition):
        """
        décryptage en ajoutant le décalage de la clé au crypto
        crypto et alpha : alphabétique (str)
        cle : numérique (array de int)
        """        

        resultat = ""
        k = 0
        
        for i, lettre in enumerate(crypto):
            
            if alpha.lower().find(lettre.lower()) >= 0: # and alpha.lower().find(cle.lower()[k % len(cle)]) >= 0:
                if addition:
                    lettre_deco =  alpha.lower().index(lettre.lower()) + cle[k % len(cle)]
                else:
                    lettre_deco =  alpha.lower().index(lettre.lower()) - cle[k % len(cle)]
                
                lettre_deco %= 26                
                if lettre.islower():
                    resultat += alpha.lower()[lettre_deco]
                else:
                    resultat += alpha.upper()[lettre_deco]
                k += 1
            else:
                resultat += lettre
                    
        return resultat
        
