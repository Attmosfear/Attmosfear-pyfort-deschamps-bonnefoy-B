#Attmosfear-pyfort-deschamps-bonnefoy-B, Deschamps Malo, Enigmes du Pere Fouras
import json
from random import *


def charger_enigmes(fichier):
    """
    Cette fonction recupere les informations du fichier json au bon format
    :param fichier: recupere l'emplacement du fichier
    :return: Un tableau avec les informations du fichier extraitent dans le bon format
    """
    with open(fichier, 'r', encoding="utf-8") as f:
        return json.load(f)

def enigme_pere_fouras():
    """
    Cette fonction est la fonction principale, elle pose l'enigme au joueur qui doit trouver la bonne reponse
    :return: retourne si le joueur a gagné (True) ou s'il a perdu (False)
    """

    # Recuperation de la question et affichage
    enigmes = charger_enigmes('Data/enigmesPF.json')
    enigme = enigmes[randint(0,len(enigmes)-1)]
    print("Voici l'enigme :")
    print(enigme['question'])
    # Recuperation de la reponse du joueur puis verification avec 3 essaies
    essaies = 3
    while essaies > 0:
        reponse = input('Veuillez saisir la reponse : ')
        reponse = reponse.lower()
        if reponse == enigme['reponse'].lower():
            if enigme['type'] == "clé":
                print("Bravo ! Vous avez gagner une clé")
                return True
            else:
                print("Bravo ! Vous avez gagner un indice")
                return True
        else:
            essaies -= 1
            if essaies != 0:
                print("Reponse incorrecte")
                print("Il vous reste", essaies, "essaies")
            if essaies == 0:
                print("Vous avez echoué")
                print("Voici la réponse :", enigme['reponse'])
                return False
