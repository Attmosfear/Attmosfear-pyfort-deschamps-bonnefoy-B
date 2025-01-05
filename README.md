# Attmosfear-pyfort-deschamps-bonnefoy-B

1. Présentation Générale :

Titre du Projet : Fort Boyard Simulator

- Contributeurs : Malo Deschamps, Florian Bonnefoy

- Description : Création d'un jeu reprenant l'idée du jeu Fort Boyard avec 4 épreuves jouable en équipe de 1 à 3 joueurs.

- Fonctionnalités Principales : 

    Formation d'une équipe.
    Des interraction avec l'utilisateur directement à travers la console python.
    Plusieurs épreuves disponible : mathématiques, logique, hasard, et énigmes.
    Sauvegarde du score de chaque utilisateur.


- Technologies Utilisées :

    Language de programmation : Python
    Bibliothèques utilisé : Random, JSON
    Outil: PyCharm Community Edition
    

- Installation :
    
  Pour le clone : URL -> Code -> HTTPS sur GitHub et le copier
  Dans PyCharm menus -> Git -> Clone...
  Coller l'URL -> Cloner

- Utilisation :

    Pour lancer le programme principale : exécutez le programme : main.py .

2. Documentation Technique

- Algorithme du jeu :

    1 ) Présentation des règles du jeu avec la fonction introduction().
    2 ) Création de l'équipe avec la fonction composer_equipe().
    3 ) Sélection aléatoire d'une épreuves parmi celles disponibles : énigmes, mathématiques, logique et hasard.
    4 ) vérification de la réponse des joueurs.
    5 ) Comptage des clés et du score des joueurs.
    6 ) Détermine la victoire ou la défaite, ainsi que l'affichage des résultats.

- Détails des fonctions :

    main.py :
      - jeu() Fonction principale qui rassemble toutes les fonctions du jeu
    
    fonctions_utiles.py :
      - introduction() Fonction qui affiche les règles du jeu.
      - composer_equipe() Foncrion qui permet à l'utilisateur de faire une équipe de 1 à 3 personnes, elle renvoie une liste de dictionnaires.
      - menu_epreuves() Fonction qui affiche à l'utilisateur la liste des épreuves disponible et lui demande de choisir, elle renvoie un entier.
      - choisir_joueur(equipe) Fonction qui affiche la liste de joueurs et demande de choisir quelle joueur souhaite participé à l'epreuve, elle renvoie un entier.

    epreuves_mathématiques.py :
      - epreuve_math_factorielle() lance l'épreuve factorielle, elle renvoie un Booléen.
      - resoudre_equation_lineaire() Créée une équation linéaire aléatoire, elle renvoie un string et deux entiers.
      - epreuve_math_equation() lance l'epreuve d'equation linéaire, elle renvoie un Booléen.
      - roulette_maths() lance l'epreuve de roulette, aléatoirement : addition, soustraction, multiplication, division, elle renvoie un Booléen.
      - epreuve_maths() choisit une des epreuves de math au hasard.

    epreuves_hasard.py :
      - bonneteau() lance l'epreuve des Bonneteaux, elle renvoie un Booléen.
      - jeu_lance_des() lance l'epreuve de lancé de dés, elle renvoie un Booléen.
      - epreuve_hasard() Choisit une des deux epreuves au hasard.

    epreuves_logiques.py :
      - suiv(joueur) renvoie un entier qui représente le joueur 0 ou 1.
      - grille_vide() Initialise une matrice vide de 3x3, elle renvoie une liste (2D).
      - affiche_grille(grille,message) affiche une grille de jeu pour le joueur.
      - demande_position() Demande une position sur la matrice au joueur sous la forme de coordonnée x et y.
      - init() Permet au joueur d'initialiser sa grille de jeu, renvoie une liste (2D).
      - tour(joueur, grille_tirs_joueur, grille_adversaire) Effectue un tour de jeu, renvoie une grille avec le tir du joueur.
      - gagne(grille_tirs_joueur) Verfie si le joueur a gagné ou non et renvoie un Booléen.
      - jeu_bataille_navale() Lance l'epreuve renvoie un Booléen.

    enigmes_pere_fouras :
      - charger_enigmes(fichier) Charge les données du fichier enigmes.json, renvoie une liste de dictionnaires
      - enigme_pere_fouras() Permet le déroulement de l'epreuve d'énigmes. return un Booléen

    Epreuve_finale.py :
      - salle_De_Tresor() lance l'epreuve de salle du trésor., renvoie un Booléen.


