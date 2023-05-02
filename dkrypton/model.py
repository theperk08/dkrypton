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
    

    def casse_vigenere(chaine, longueur = []):
        print('longueurs', longueur)
        # pour les longueurs possibles de clés
        liste_max = []
        # si pas de longueur de clé suggéré        
        if longueur == []:

            # longueur des séquences répétées à rechercher
            long_seq = 3
            # pour stocker les longueurs de clé possibles
            dico_div = {}

            

            for k in range(len(chaine) - long_seq):
                tri = chaine[k : k + long_seq]
                liste_tri = [k]
                for j in range(k + 1, len(chaine) - long_seq):
                    if chaine[j : j + long_seq] == tri:
                        liste_tri += [j - liste_tri[-1]]

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

            print(dico_div)

            liste_max = []
            maxi_occu = max(dico_div.values())
            for key, value in dico_div.items():
                if value == maxi_occu:
                    liste_max += [str(key)]  #pour affiche sous forme de string
            print(liste_max)

            
                    
            try:
                maxi = max(dico_div, key = dico_div.get)
            except:
                maxi = 0
            
            print('Longueur(s) probable(s) de la clé : ', " ; ".join(liste_max))

            longueur = liste_max

        # si longueur suggérée ou si on a trouvé une longueur possible de la clé juste avant
        longueurs = longueur
        cles =[]
        if len(longueur) > 0 :
            
        
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            

            for j in longueur:
                cle = ""
                dico = {}

                for i in range(int(j)):
                    # on split tous les 'longueur de clé' caractères
                    chaine_cle = [chaine[k] for k in range(i,len(chaine), int(j))]
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
                cles += [cle]
                print("Pour une longueur de {}, la clé est alors : {}".format(j, cle))
        # on renvoit les clés, auxquelles il faudra appliquer un décalage de César - 4
        return longueurs, cles
            

    def diviseurs(nombre):
        """
        renvoie la liste des diviseurs d'un nombre
        """
        liste = []
        for n in range(2, int(nombre//2)):
            if nombre % n == 0:
                liste += [n]

        return n
        
