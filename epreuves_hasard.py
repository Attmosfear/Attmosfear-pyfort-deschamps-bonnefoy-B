from random import *
import random

def jeu_lance_des():
    nbr_essais = 1

    while nbr_essais < 4 :
        print("Essai",nbr_essais,"sur 3")
        input("Appuyez sur Entrée pour lancer les dés...")

        des_joueur = (random.randint(1, 6), random.randint(1, 6))
        print("Le joueur a obtenu :", des_joueur[0], "et", des_joueur[1])
        if 6 in des_joueur :
            print("Félicitations ! Le joueur a obtenu un 6 il remporte la partie et gagne une clé. ")
            return True

        des_maitre = (random.randint(1, 6), random.randint(1, 6))
        print("Le maitre du jeu a obtenu :", des_maitre[0], "et", des_maitre[1])
        if 6 in des_maitre :
            print("Le maître du jeu a obtenu un 6 et remporte la partie ! Le joueur a perdu la partie.")
            return False

        nbr_essais += 1

        if 6 not in des_maitre and des_joueur :
            print("Aucun 6 obtenu, on passe au prochain essai.")

    print("Aucun joueur n'a obtenu un 6 après 3 essais. C'est un match nul !")
    return False

