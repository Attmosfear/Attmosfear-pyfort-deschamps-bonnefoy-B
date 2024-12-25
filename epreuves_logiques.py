from random import *


def suiv(joueur):
    if joueur == 0:
        return 1
    else:
        return 0

def grille_vide():
    grille = [[" "for _ in range(3)]for _ in range(3)]
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
    for pos in position_tab:
        if int(pos) < 1 or int(pos) > 3:
            return False
    position_tuple = tuple(int(x)-1 for x in position_tab)
    return position_tuple

def init():
    grille = grille_vide()
    print("Positionnez vos bateaux :")
    for i in range(1,3):
        print("Bateau", i)
        pos = demande_position()
        if grille[pos[0]][pos[1]] == " ":
            grille[pos[0]][pos[1]] = "B"
    return grille

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

#tour(1, grille_vide(), grille_vide())

def gagne(grille_tirs_joueur):
    touche = 0
    for i in range(1,3):
        for j in range(1,3):
            if grille_tirs_joueur[i][j] == "x":
                touche += 1
    if touche <= 2:
        return True
    else:
        return False