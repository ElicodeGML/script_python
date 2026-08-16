 # import random
 # import math

 # note_ia = []
 # for i in range(10):
 #     chiffre = random.randint(0, 20)
 #     note_ia.append(chiffre)

 # print(note_ia)


 # def analyser_performance(liste):
 #     max_note = max(note_ia)
 #     membre = {"moyenne_ia": sum(note_ia) / len(note_ia), "carre_ia": math.sqrt(max_note)}
 #     decision = (note_ia(i))
 #     print(f"La moyenne de X est {i["moyenne_ia"]} et la racinne carré de Y est {i["carre_ia"]} ")
import random
import math

prix_article = []

for i in range(5):
    prix = random.randint(10, 100)
    prix_article.append(prix)

def analyse_panier(liste_prix):
    total_prix = sum(prix_article)
    moyenne_prix = round(total_prix / len(prix_article), 2)
    best_prix = max(prix_article)
    reduc_prix = round(math.sqrt(best_prix), 2)
    return{
        "total": total_prix,
          "moyenne": moyenne_prix,
            "reduc": reduc_prix
}
stat = analyse_panier(prix_article)

print(f"""Le total des prix est {stat['total']} €.
La moyenne est {stat['moyenne']} €.
La racine carré du prix le plus cher {stat['reduc']} €.""")
