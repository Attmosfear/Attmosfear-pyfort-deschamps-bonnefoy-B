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



def bonneteau() :
    bonneteaux = ['A','B','C']
    max_tentatives = 2

    print("Bienvenue au jeu de bonneteau ! Voici les règles : \nUne clé est cachée sous l'un des bonneteaux le A, le B ou le C et vous devez simplement la retrouver en 2 essais.\n")
    print("Les bonneteaux disponibles sont donc : A B C")

    for i in range(1, max_tentatives + 1):
        bonneteau_choisi = bonneteaux[random.randint(0, len(bonneteaux) - 1)]
        print("\nTentative" ,i, "sur",max_tentatives,".")
        choix_joueur = input("Choisissez un bonneteau A, B ou C : ").upper()

        if choix_joueur in bonneteaux:
            if choix_joueur == bonneteau_choisi:
                print("Bravo ! Vous avez trouvé la clé sous le bonneteau",bonneteau_choisi,".")
                return True
            else:
                print("Rater, la clé ne se trouvait pas sous ce bonneteau.")
        else:
            print("Choix invalide. Veuillez entrer A, B ou C.")

        print("Vous avez perdu ! La clé se trouvait sous le bonneteau",bonneteau_choisi ,".")
        return False

def epreuve_hasard():
    epreuves = [jeu_lance_des, bonneteau]
    epreuve = epreuves[random.randint(0, len(epreuves) - 1)]
    epreuve()
