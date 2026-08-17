# ============================================
# JEU DU PENDU
# ============================================

def pendue(mot_mystere, nb_vie):
    """
    Jeu du pendu où l'utilisateur doit deviner un mot lettre par lettre.
    
    Args:
        mot_mystere (str): Le mot à deviner
        nb_vie (int): Nombre de vies (tentatives incorrectes)
    """
    # Initialiser le mot public avec des tirets
    mot_public = '_' * len(mot_mystere)

    # Boucle principale du jeu
    while nb_vie > 0 and mot_mystere != mot_public:
        lettre = input('Entrez une lettre : ')

        # Vérifier si la lettre est dans le mot mystère
        if lettre in mot_mystere:
            # Révéler toutes les occurrences de la lettre
            for i in range(len(mot_mystere)):
                if mot_mystere[i] == lettre:
                    mot_public = mot_public[:i] + lettre + mot_public[i + 1:]
        else: 
            # Perdre une vie si la lettre n'est pas trouvée
            nb_vie -= 1

        # Afficher l'état du jeu
        if mot_public == mot_mystere:
            print(f"Bravo ! Le mot est {mot_mystere}.")
        elif nb_vie == 0:
            print("Vous avez perdu")
        else:
            print(f"Vous avez {nb_vie} vie(s)")
            print(f"Il reste {mot_public.count('_')} lettre(s) à trouver")
            print(f"Le mot est : {mot_public}")

# pendue('salut', 5)

# ============================================
# FONCTION DE DESSIN AVEC SYMBOLES
# ============================================

def joli(symbole_2, nb, symbole):
    """
    Crée un motif graphique en remplaçant progressivement les caractères.
    
    Args:
        symbole_2 (str): Caractère de remplacement
        nb (int): Nombre de caractères à afficher
        symbole (str): Caractère initial
    """
    # Afficher la première ligne avec le symbole initial
    mot = symbole * nb
    print(mot)
    
    # Remplacer progressivement chaque caractère
    for i in range(len(mot)):
        mot = mot[:i] + symbole_2 + mot[i + 1:]
        print(mot)

# Exécuter la fonction joli
joli('6', 39, '9')