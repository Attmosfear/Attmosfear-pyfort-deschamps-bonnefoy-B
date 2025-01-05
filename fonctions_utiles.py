def introduction():
    print("Bienvenue dans le Fort Boyard Simulator ! 🎉")
    print("En bref, c'est Fort Boyard sauf que vous n'etes pas connus, nous n'avons pas de budget donc vous n'etes pas filmé")
    print("Cependant, il y a quand meme un prix à gagné")
    print("Alors, Bonne chance !!! ")
    print("Voici les règles de base :")
    print("1. Vous devez accomplir des épreuves pour gagner des clés.")
    print("2. Ramassez trois clés pour accéder à la salle du trésor.")
    print("3. Déverrouillez la salle du trésor pour remporter la victoire ! 🏆")

def composer_equipe():
    print("C'est l'heure de composer votre équipe ! 🧑‍🤝‍🧑")
    equipe = []
    #Recuperation du nombre de joueur
    while True:
        try:
            nb_joueurs = int(input("Combien de joueurs souhaitez-vous inscrire ? (maximum 3) : "))
            if 1 <= nb_joueurs <= 3:
                break
            print("Le nombre de joueurs doit être entre 1 et 3. Réessayez.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    #Recuperation des informations du joueurs
    for i in range(nb_joueurs):
        print(f"\nJoueur {i + 1} :")
        nom = input("Nom du joueur : ").strip()
        profession = input("Profession du joueur : ").strip()
        while True:
            leader = input("Ce joueur est-il le leader de l'équipe ? (oui/non) : ").strip().lower()
            if leader in ["oui", "non"]:
                break
            print("Veuillez répondre par 'oui' ou 'non'.")

        joueur = {
            "nom": nom,
            "profession": profession,
            "leader": leader == "oui",
            "cles_gagnees": 0
        }
        equipe.append(joueur)
    #Verification du leader
    if not any(joueur["leader"] for joueur in equipe):
        print("Aucun leader désigné. Le premier joueur sera automatiquement le leader.")
        equipe[0]["leader"] = True

    print("\nVotre équipe est prête à relever les défis ! Voici les membres de votre équipe :")
    for joueur in equipe:
        status = "Leader" if joueur["leader"] else "Membre"
        print(f"- {joueur['nom']} ({status}), Profession : {joueur['profession']}, Clés gagnées : {joueur['cles_gagnees']}")

    return equipe


def menu_epreuves():
    print("\n=== Menu des Épreuves ===")
    print("\n1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du Hasard")
    print("4. Énigme du Père Fouras\n")

    while True:
        try:
            choix = int(input("Choisissez une épreuve (1-4) : "))
            if 1 <= choix <= 4:
                return choix
            print("Veuillez choisir un nombre entre 1 et 4.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
def choisir_joueur(equipe):
    print("\n=== Sélection d'un Joueur ===")
    i = 0
    for joueur in equipe:
        i += 1
        if joueur["leader"]:
            role = "Leader"
        else:
            role = "Membre"
        print(f"{i}. {joueur['nom']} ({joueur['profession']}) - {role}")

    while True:
        try:
            num_joueur = int(input("Entrez le numéro du joueur qui participera à l'épreuve : "))
            if 1 <= num_joueur <= len(equipe):
                joueur_selectionne = equipe[num_joueur - 1]
                print(f"Joueur sélectionné : {joueur_selectionne['nom']} ({joueur_selectionne['profession']})")
                return joueur_selectionne
            print("Veuillez entrer un numéro valide.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
