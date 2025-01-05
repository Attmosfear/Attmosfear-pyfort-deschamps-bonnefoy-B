#Attmosfear-pyfort-deschamps-bonnefoy-B, Deschamps Malo et Florian Bonnefoy, Epreuve de Mathematiques
from random import *
import random

def factorielle(n) :
    resultat = 1
    if n == 0 :
        return(resultat)
    else :
        for i in range (1, n+1):
            resultat = resultat * i
    return(resultat)

def epreuve_math_factorielle():
    a = randint(1, 10)
    print("Calculer la factorielle de",a)
    reponse = int(input("Votre réponse est :"))
    if reponse == factorielle(a):
        return True
    else:
        return False


def resoudre_equation_lineaire():
    """
    Cette fonction permet de creer et resoudre une equation lineaire
    :return: retourne les 2 coefficients ainsi que l'inconnue
    """
    a = randint(1,10)
    b = randint(1,10)
    x = -b/a
    return  a, b, x

def epreuve_math_equation():
    """
    Cette fonction permet de demander au joueur la valeur de l'inconnue et de verifier si elle est correcte
    :return: Retourne si le valeur est correcte (True) et si elle est incorrecte (False)
    """
    res, a, b = resoudre_equation_lineaire()
    print("Résoudre l'équation : ", a,"x + ", b, "= 0" )
    val = float(input("Quelle est la valeur de x:"))
    if val == res:
        return True
    else:
        return False

def epreuve_roulette_mathematique():
    """
    Cette fonction corresponds a l'epreuve de la roulette, c'est a dire, une +, - ou x a calculé par le joueur
    :return: retourne si la reponse du joueur corresponds a la reponse demandé (True) et inversement (False)
    """
    tableau_nombre = []
    # Selection aleatoire des 5 nombres pour le calcul
    for i in range(5):
        tableau_nombre.append(randint(1, 20))
    print("Nombre de la roulette : ", tableau_nombre)
    # Selection aleatoire de l'opération pour le calcul
    tableau_opp = ['+', '-', 'x']
    index = randint(0, len(tableau_opp)-1)
    opp = tableau_opp[index]
    # Calcule du resultat selon l'operation
    if opp == '+':
        res = 0
        for i in range(0, len(tableau_nombre)):
            res = res + tableau_nombre[i]
        print("Calculez le résultat en combinant ces nombres avec une addition")
    elif opp == '-':
        res = 0
        for i in range(0, len(tableau_nombre)):
            res = res - tableau_nombre[i]
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
    else:
        res = 1
        for i in range(0, len(tableau_nombre)):
            res = res * tableau_nombre[i]
        print("Calculez le résultat en combinant ces nombres avec une multiplication")
    # Recuperation et verification de la reponse du joueur
    proposition = int(input("Votre réponse : "))
    if  proposition != res:
        return False
    return True

def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def premier_plus_proche(n):
    while not est_premier(n):
        n += 1
    return n

def epreuve_math_premier():
    x = random.randint(10, 20)
    print("Trouver le nombre premier le plus proche de", x, ":")
    reponse = int(input("Votre réponse : "))
    solution = premier_plus_proche(x)
    if reponse == solution:
        print("Correct !")
        return True
    else:
        print("Faux. La bonne réponse était", solution)
        return False

def epreuve_math():
    epreuves = [epreuve_math_equation, epreuve_math_factorielle,epreuve_roulette_mathematique, epreuve_math_premier]
    epreuve = epreuves[randint(0, len(epreuves)-1)]
    print("Épreuve de Mathématiques:")
    epreuve()