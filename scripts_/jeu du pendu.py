def pendue(x, y):
    mot_mystere = x

    nb_vie = y

    mot_public = '_' * len(mot_mystere)

    while nb_vie > 0 and mot_mystere != mot_public:
        lettre = input ('entrez une lettre : ')

        if lettre in mot_mystere:
            for i in range(len(mot_mystere)):
                if mot_mystere[i] == lettre:
                    mot_public = mot_public[:i] + lettre + mot_public[i +1:]
        else: 
            nb_vie -= 1

        if mot_public == mot_mystere:
            print("Bravo ! Le mot est", mot_mystere,".")
        elif nb_vie == 0:
            print("vous avez perdue")
        else:
            print("Vous avez", nb_vie, "vie")
            print("Il reste", mot_public.count('_'),"lettre à trouver")
            print("Le mot est:", mot_public)
        
# pendue('salut', 5)

def joli(x, y, z):
    symbole = z
    nb = y
    symbole_2 = x
    mot = symbole*nb
    print(mot)
    for i in range(len(mot)):
        mot = mot[:i]+symbole_2+mot[i +1:]
        print(mot)

joli('6', 39, '9')