from operator import is_not
from random import *
import random
from math import*


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
    print("Épreuve de Mathématiques: Calculer la factorielle de",a)
    reponse = int(input("Votre réponse est :"))
    if reponse == factorielle(a):
        return True
    else:
        return False


def resoudre_equation_lineaire():
    a = randint(1,10)
    b = randint(1,10)
    x = -b/a
    return  a, b, x

def epreuve_math_equation():
    res, a, b = resoudre_equation_lineaire()
    print("Résoudre l'équation : ", a,"x + ", b, "= 0" )
    val = float(input("Quelle est la valeur de x:"))
    if val == res:
        return True
    else:
        return False

def epreuve_roulette_mathematique():
    tableau_nombre = []
    res = 0
    for i in range(5):
        tableau_nombre.append(randint(1, 20))
    print("Nombre de la roulette : ", tableau_nombre)
    tableau_opp = ['+', '-', 'x']
    index = randint(0, len(tableau_opp)-1)
    opp = tableau_opp[index]
    if opp == '+':
        for i in range(len(tableau_nombre)):
            res = 0
            res =+ tableau_nombre[i]
        print("Calculez le résultat en combinant ces nombres avec une addition")
    elif opp == '-':
        for i in range(len(tableau_nombre)):
            res = 0
            res =- tableau_nombre[i]
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
    else:
        for i in range(len(tableau_nombre)):
            res = 1
            res = res * tableau_nombre[i]
        print("Calculez le résultat en combinant ces nombres avec une multiplication")

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
        n = n + 1
    return n

print(epreuve_roulette_mathematique())