# model.py
import plotly.express as px

class Models:
    def __init__(self):
        pass

    

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

    def calcul_IC(dico, total):
        """
        fonction qui calcule l'IC
        en prenant un dico du nombre d'apparitions des lettres
        et la longueur total de la chaîne étudiée
        """
        
        IC = 0
        for value in dico.values():
            IC += value * (value -1)

        IC = IC/(total * (total - 1))

        return IC
    

    def casse_vigenere(chaine, freq_theorique):

        long = 1
        # pour stocker les longueurs de clé possibles
        dico_div = {}

        for k in range(len(chaine)-3):
            tri = chaine[k:k+3]
            liste_tri = [k]
            for j in range(k+1, len(chaine)-3):
                if chaine[j:j+3] == tri:
                    liste_tri += [j-liste_tri[-1]]

            if len(liste_tri) > 1:
                for nombre in liste_tri[1:]:
                    liste = []
                    for divi in range(2, int(nombre//2)):
                        if nombre % divi == 0:
                            liste += [divi]
                    
                    for a in liste:
                        if a in dico_div.keys():
                            dico_div[a] += 1
                        else:
                            dico_div[a] = 1
                
        maxi = max(dico_div, key = dico_div.get)
        
        print('Longueur probable de la clé :', maxi)
        

        dico = {}
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        cle = ""

        for i in range(maxi):
            # on split tous les 'longueur de clé' caractères
            chaine_cle = [chaine[k] for k in range(i,len(chaine), maxi)]
            chaine_cle = "".join(chaine_cle)
            # pour faire une analyse de fréquence
            for lettre in alphabet:
                dico[lettre] = 0
            for lettre in chaine_cle:
                try:
                    dico[lettre] += 1
                except:
                    pass
            # sachant que la lettre la plus courante est un E
            cle += max(dico, key = dico.get)
            

        print("La clé est alors :", cle)
        # on renvoit la clé, à laquelle il faudra appliquer un décalage de César - 4
        return maxi, cle
            

    def diviseurs(nombre):
        """
        renvoie la liste des diviseurs d'un nombre
        """
        liste = []
        for n in range(2, int(nombre//2)):
            if nombre % n == 0:
                liste += [n]

        return n
        
