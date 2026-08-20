import random
import math

prix_article = []

for i in range(5):
    prix = random.randint(10, 100)
    prix_article.append(prix)

def analyse_panier(liste_prix):
    total_prix = sum(liste_prix)
    moyenne_prix = round(total_prix / len(liste_prix), 2)
    best_prix = max(liste_prix)
    reduc_prix = round(math.sqrt(best_prix), 2)
    return {
        "total": total_prix,
        "moyenne": moyenne_prix,
        "reduc": reduc_prix
    }

stat = analyse_panier(prix_article)

print(f"""Le total des prix est {stat['total']} €.
La moyenne est {stat['moyenne']} €.
La racine carré du prix le plus cher {stat['reduc']} €.""")