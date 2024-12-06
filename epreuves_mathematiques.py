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



