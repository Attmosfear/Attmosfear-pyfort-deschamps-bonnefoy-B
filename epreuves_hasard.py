#Attmosfear-pyfort-deschamps-bonnefoy-B ; Florian Bonnefoy ; Epreuve de hasard
from random import *
import random


# Role de la fonction jeu_lance_des : Un joueur et un maître lancent des dés pour obtenir un 6 en trois essais max. Le premier à faire un 6 gagne.
# La fonction ne prend aucun pramètre en entrée.
# Résultat renvoyé : True si le joueur fait un 6 et False si le joueur ne parvient pas a faire 6 avant le maitre du jeu.

def jeu_lance_des():
    nbr_essais = 1

    # Initialisation du nombre d'essais
    while nbr_essais < 4 :
        print("Essai",nbr_essais,"sur 3")
        input("Appuyez sur Entrée pour lancer les dés...")

        # Lancer de dés pour le joueur
        des_joueur = (random.randint(1, 6), random.randint(1, 6))
        print("Le joueur a obtenu :", des_joueur[0], "et", des_joueur[1])

        # Vérifie si le joueur a obtenu un 6
        if 6 in des_joueur :
            print("Félicitations ! Le joueur a obtenu un 6 il remporte la partie et gagne une clé. ")
            return True

        # Lancer de dés pour le maître du jeu
        des_maitre = (random.randint(1, 6), random.randint(1, 6))
        print("Le maitre du jeu a obtenu :", des_maitre[0], "et", des_maitre[1])

        # Vérifie si le maître du jeu a obtenu un 6
        if 6 in des_maitre :
            print("Le maître du jeu a obtenu un 6 et remporte la partie ! Le joueur a perdu la partie.")
            return False

        # Incrémentation du compteur d'essais
        nbr_essais += 1

        # Message si aucun 6 n'a été obtenu
        if 6 not in des_maitre and des_joueur :
            print("Aucun 6 obtenu, on passe au prochain essai.")

    # MessagesSi aucun joueur n'obtient un 6 après 3 essais
    print("Aucun joueur n'a obtenu un 6 après 3 essais. C'est un match nul !")
    return False


# Role dela fonction bonneteau : Le joueur devine sous quel bonneteau A, B ou C est cachée la clé en deux tentatives.
# La fonction ne prend aucun paramètre en entrée.
# Résultat renvoyé : True si le joueur trouve la clé en 2 essais et False si il ne la trouve pas

def bonneteau() :
    #Liste des bonneteaux disponibles et nombre max de tentatives.
    bonneteaux = ['A','B','C']
    max_tentatives = 2

    # Règles du jeu
    print("Bienvenue au jeu de bonneteau ! Voici les règles : \nUne clé est cachée sous l'un des bonneteaux le A, le B ou le C et vous devez simplement la retrouver en 2 essais.\n")
    print("Les bonneteaux disponibles sont donc : A B C")

    # Boucle pour gérer les tentatives du joueur
    for i in range(1, max_tentatives + 1):
        # Sélection aléatoire du bonneteau contenant la clé
        bonneteau_choisi = bonneteaux[random.randint(0, len(bonneteaux) - 1)]
        print("\nTentative" ,i, "sur",max_tentatives,".")
        # Demande au joueur de choisir un bonneteau
        choix_joueur = input("Choisissez un bonneteau A, B ou C : ").upper()

        # Vérifie si l'entrée du joueur est valide
        if choix_joueur in bonneteaux:
            # Vérifie si le choix du joueur est correct
            if choix_joueur == bonneteau_choisi:
                print("Bravo ! Vous avez trouvé la clé sous le bonneteau",bonneteau_choisi,".")
                return True
            else:
                print("Rater, la clé ne se trouvait pas sous ce bonneteau.")
        else:
            print("Choix invalide. Veuillez entrer A, B ou C.")

        # Message si le joueur échoue à trouver la clé après toutes les tentatives
        print("Vous avez perdu ! La clé se trouvait sous le bonneteau",bonneteau_choisi ,".")
        return False

# Sélectionne et lance un mini-jeu aléatoire parmi une liste.
# La fonction ne prend aucun paramètre en entrée.
# Résultat renvoyé : la fonction ne renvoie rien simplement True ou False par l'appel des 2 fonctions précédente.

def epreuve_hasard():
    # Sélection aléatoire d'une épreuve puis l'execute.
    epreuves = [jeu_lance_des, bonneteau]
    epreuve = epreuves[random.randint(0, len(epreuves) - 1)]
    epreuve()
