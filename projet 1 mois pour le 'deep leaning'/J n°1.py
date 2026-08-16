score = [12, 8, 15, 20, 4, 10, 3]
admis = []
recales = []

print(score, admis, recales)

for i in score:
    if i >= 10:
        admis.append(i)
    else:
        recales.append(i)

print(score, admis, recales)

moyenne_score = round(sum(score) / len(score), 2)
moyenne_admis = round(sum(admis) / len(admis), 2)
valeur_max = max(score)
valeur_min = min(score)

nb_lettre_dans_recales = len(recales)
if nb_lettre_dans_recales == 0:
    moyenne_recales = ("Il n'y a pas de note en dessous de zéro")
else:
    moyenne_recales = round(sum(recales) / nb_lettre_dans_recales, 2)

if moyenne_score >= 10 and valeur_min >= 5:
    print("Resultat global reussit")
else:
    print("Resultat global échec")


print("Ma moyenne est", moyenne_score, "Ma moyenne haute est",  moyenne_admis, "Mamoyenne basse est", moyenne_recales)
