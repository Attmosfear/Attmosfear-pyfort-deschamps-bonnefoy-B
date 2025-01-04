import json
from random import *


def charger_enigmes(fichier):
    with open(fichier, 'r', encoding="utf-8") as f:
        return json.load(f)

def enigme_pere_fouras():
    enigmes = charger_enigmes('Data/enigmesPF.json')
    enigme = enigmes[randint(0,len(enigmes)-1)]
    essaies = 3
    print("Voici l'enigme :")
    print(enigme['question'])
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
