import numpy as np
                             


def format_texte(texte):
    """
    Transformation d'un texte qui sera renvoyé au format :
    - en une seule ligne
    - en majuscule
    - sans accent
    - ni autres caractères    
    """

    # récupère toutes les lignes
    texte = str(texte).splitlines()
    # pour n'en faire qu'une seule
    texte = ''.join(texte)

    # suppression des autres caractères
    caract = ',.-_()[] \'"'
    
    for cara in caract:
        texte = texte.replace(cara,'')
        
    ### suppression des accentes et cédilles
    accents = "ÂÁÀÃÉÈËÊÎÏÔÕÙÜÛÇÑ"
    equivalents = "AAAAEEEEIIOOUUUCN"

    # après avoir mis tout en majuscule
    texte_format = texte.upper()
    for accent, lettre in zip(accents, equivalents):
        texte_format = texte_format.replace(accent, lettre)
    
    print(texte_format)
    return texte_format

def compteLettres(texte, alphabet):
    dico_lettre = {}
    for lettre in alphabet:
        dico_lettre[lettre] = 0
    for lettre in texte:
        try:
            dico_lettre[lettre] += 1
        except:
            pass

    return dico_lettre

def freqenceLettres(liste):
    pass


