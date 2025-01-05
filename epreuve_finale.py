#Attmosfear-pyfort-deschamps-bonnefoy-B ; Deschamps Malo et Floriant Bonnefoy ; Epreuve finale
import json
import random


def salle_De_Tresor():
    """
    Cette fonction correspond a l'epreuve finale du jeu (elle est appelé en dernier)
    :return: Elle ne retourne rien car elle permet de cloturer le jeu
    """

    with open('Data/indicesSalle.json', 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)
    # Recuperation des informations
    annees = list(jeu_tv["Fort Boyard"].keys())
    annee = random.choice(annees)

    emissions = jeu_tv["Fort Boyard"][annee]
    emission_name = random.choice(list(emissions.keys()))

    indices = emissions[emission_name]["Indices"]
    mot_code = emissions[emission_name]["MOT-CODE"]

    print(f"Voici les trois premiers indices pour l'émission {emission_name} ({annee}) :")
    for i in range(3):
        print(f"- {indices[i]}")

    essais = 3
    reponse_correcte = False
    i = 0
    # Recuperation de la reponse du joueur et verification de celle-ci
    while essais > 0:
        reponse = input(f"Essayez de deviner le mot-code (essais restants: {essais}): ").strip().upper()

        if reponse == mot_code:
            reponse_correcte = True
            break
        else:
            i += 1
            essais -= 1
            if essais > 0:
                print(f"Ce n'est pas le bon mot-code. Il vous reste {essais} essais.")
                print(f"Nouvel indice : {indices[3 + i]}")
            else:
                print(f"Vous avez échoué. Le mot-code était : {mot_code}")

    # Affichage final
    if reponse_correcte:
        print(f"Félicitations ! Vous avez trouvé le mot-code : {mot_code}")
        print("\n Vous pensez vraiment que nous avons le budget pour un tresor")
        print("Prenez ces pieces en chocolats, c'est déjà ça")
    else:
        print(f"Dommage, vous n'avez pas réussi. Le mot-code était : {mot_code}")
        print("Au mince, si proche du but")
        print("Vous reviendrez plus fort la prochaine fois")
        print("HAHAHAHAHAHAHHAHAHAHAHA")
