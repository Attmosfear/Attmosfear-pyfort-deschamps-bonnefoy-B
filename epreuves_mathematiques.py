from random import *
def resoudre_equation_lineaire():
    a = randint(1,10)
    b = randint(1,10)
    x = -b/a
    return  a, b, x

def epreuve_math_equation():
    res, a, b = resoudre_equation_lineaire()
    print(" Résoudre l'équation : ", a,"x + ", b, " = 0" )
    val = float(input("Quelle est la valeur de x:"))
    if val == res:
        return True
    else:
        return False

def epreuve_roulette_mathematique():
    tableau_nombre = [randint(1, 20)]*5
    opp = random('+', '-', 'x')
    if opp == '+':
        for i in range(len(tableau_nombre)):
            res =+ tableau_nombre[i]
    elif opp == '-':
        for i in range(len(tableau_nombre)):
            res =- tableau_nombre[i]
    else:
        for i in range(len(tableau_nombre)):
            res = 1
            res = res * tableau_nombre[i]








