from random import *

def suiv(joueur):
    if joueur == 0:
        return 1
    else:
        return 0

def grille_vide(taille_plateau = 3):
    grille = [[" "for _ in range(taille_plateau)]for _ in range(taille_plateau)]
    return grille

def affiche_grille(grille, message):
    print(message)
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            print("|", end=" ")
            print(grille[i][j], end=" ")
        print("|", end="")
        print()
    print("-------------")

def demande_position():
    position = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) : ")
    position_tab = position.split(",")
    if len(position_tab) != 2:
        print("Mauvais format de position")
        return demande_position()
    for pos in position_tab:
        if int(pos) < 1 or int(pos) > 3:
            print("Mauvais format de position")
            return demande_position()
    position_tuple = tuple(int(x)-1 for x in position_tab)
    return position_tuple

def init():
    grille_joueur = grille_vide()
    # Creation de la grille de bateau du joueur
    print("Positionnez vos bateaux :")
    i = 1
    while i < 3:
        print("Bateau", i)
        pos = demande_position()
        if grille_joueur[pos[0]][pos[1]] == " ":
            grille_joueur[pos[0]][pos[1]] = "B"
            i = i + 1
        else:
            print("Un bateau se trouve deja a cette position")
    # Creation de la grille de bateau du maitre du jeu
    i = 0
    grille_maitre = grille_vide()
    while i < 2:
        pos = (randint(0, 2), randint(0, 2))
        if grille_maitre[pos[0]][pos[1]] == " ":
            grille_maitre[pos[0]][pos[1]] = "B"
            i = i + 1
    print(grille_maitre)

    return grille_joueur, grille_maitre

def tour(joueur, grille_tirs_joueur, grille_adversaire):
    if joueur == 0:
        tir = (randint(0, 2), randint(0, 2))
        print(f"Le maitre du jeu tire en position {tir[0]+1},{tir[1]+1}")
    else:
        affiche_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués :")
        tir = demande_position()
    if grille_adversaire[tir[0]][tir[1]] == " ":
        print("Dans l'eau...")
        grille_tirs_joueur[tir[0]][tir[1]] = "."
    if grille_adversaire[tir[0]][tir[1]] == "B":
        print("Touché coulé !")
        grille_tirs_joueur[tir[0]][tir[1]] = "x"

def gagne(grille_tirs):
    touche = 0
    for i in range(3):
        for j in range(3):
            if grille_tirs[i][j] == "x":
                touche += 1
    if touche >= 2:
        return True
    else:
        return False

def jeu_bataille_navale():
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. Les bateaux coulés sont marqués par 'x'.")
    grille_joueur, grille_maitre = init()
    affiche_grille(grille_joueur, "Découvrez votre grille de jeu avec vos bateaux :")
    grille_tir_joueur = grille_vide()
    grille_tir_maitre = grille_vide()
    while True:
        joueur = 1
        tour(joueur, grille_tir_joueur, grille_maitre)
        joueur = suiv(joueur)
        tour(joueur, grille_tir_maitre, grille_joueur)
        print(joueur)
        if gagne(grille_tir_joueur) is True:
            print("Le joueur a gagné !")
            return True
        if gagne(grille_tir_maitre) is True:
            print("Vous avez perdu !")
            return False

