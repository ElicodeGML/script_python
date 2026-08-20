# ==================== INITIALISATION ====================
# Liste des scores et listes de classification
score = [12, 8, 15, 20, 4, 10, 3]
admis = []
recales = []

print("État initial :", score, admis, recales)

# ==================== CLASSIFICATION DES SCORES ====================
# Séparer les scores en admis (>= 10) et recalés (< 10)
for i in score:
    if i >= 10:
        admis.append(i)
    else:
        recales.append(i)

print("Après classification :", score, admis, recales)

# ==================== CALCULS STATISTIQUES ====================
# Calculer les moyennes et valeurs extrêmes
moyenne_score = round(sum(score) / len(score), 2)
moyenne_admis = round(sum(admis) / len(admis), 2)
valeur_max = max(score)
valeur_min = min(score)

# Calculer la moyenne des recalés (avec vérification si liste vide)
nb_lettre_dans_recales = len(recales)
if nb_lettre_dans_recales == 0:
    moyenne_recales = "Il n'y a pas de note en dessous de 10"
else:
    moyenne_recales = round(sum(recales) / nb_lettre_dans_recales, 2)

resultat_global = "Le resultat global"

print("Ma moyenne est", moyenne_score, "| Ma moyenne haute est", moyenne_admis, "| Ma moyenne basse est", moyenne_recales)

# ==================== RAPPORT FINAL ====================
# Créer un dictionnaire avec les statistiques
rapport_ia = {
    "effectif": len(score),
    "moyenne": moyenne_score,
    "meilleur note": valeur_max,
    "statut": resultat_global
}

# Afficher les résultats
print("La moyenne de la classe est :", rapport_ia["moyenne"])
print("La meilleur note de la classe est :", rapport_ia["meilleur note"])
print("Le nombre d'élève dans la classe est :", rapport_ia["effectif"])

# Déterminer si le résultat est un succès ou un échec
if moyenne_score >= 10 and valeur_min >= 5:
    print(rapport_ia["statut"], "est un succès")
else:
    print(rapport_ia["statut"], "est un échec")
    