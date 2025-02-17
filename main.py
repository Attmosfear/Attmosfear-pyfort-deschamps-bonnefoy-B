#Attmosfear-pyfort-deschamps-bonnefoy-B, Deschamps Malo et Florian Bonnefoy, Epreuve Finale

from enigme_pere_fouras import enigme_pere_fouras
from epreuve_finale import salle_De_Tresor
from epreuves_hasard import epreuve_hasard
from epreuves_logiques import jeu_bataille_navale
from epreuves_mathematiques import epreuve_math
from fonctions_utiles import *



def jeu():
    """
    Cette fonction est la derniere fonction qui regroupe toutes les epreuves et l'epreuve finale
    :return: Rien car elle affiche la victoire ou la defaite de l'equipe
    """
    # Introduction
    introduction()
    equipe = composer_equipe()

    #Epreuves
    print("\n=== Début des épreuves ===")
    cles_obtenues = 0

    while cles_obtenues < 3:
        print(f"\nClés obtenues : {cles_obtenues}/3")
        choix_epreuve = menu_epreuves()
        joueur = choisir_joueur(equipe)
        reussite = False
        print(f"\n{joueur['nom']} est prêt à relever l'épreuve !")
        if choix_epreuve == 1:
            reussite = epreuve_math()
        elif choix_epreuve == 2:
            reussite = jeu_bataille_navale()
        elif choix_epreuve == 3:
            reussite = epreuve_hasard()
        elif choix_epreuve == 4:
            reussite = enigme_pere_fouras()

        if reussite:
            print("Bravo ! Vous avez gagné une clé.")
            joueur['cles_gagnees'] += 1
            cles_obtenues += 1
        else:
            print("Dommage, vous n'avez pas réussi cette fois.")

    # Epreuve finale
    print("\n=== Épreuve Finale : La Salle du Trésor ===")
    print("Vous avez maintenant accès à la salle du trésor. Répondez correctement pour gagner !")
    salle_De_Tresor()


jeu()
