class CompteProjet:
    def __init__ (self, budget_initial = 1000, p_achats = []):
        self.budget = budget_initial
        self.achat = p_achats
        print(f'le budget initial est de {budget_initial} €. ')

    def prix_dollars_depart(self):
        dollar = self.budget * 1.08
        print(f'le budget initial est de {round(dollar, 2)} $')
        
    def ajouter_fonds(self, montant):
        self.budget += montant
        print(f"{montant} € ont été ajouter")

    def depenser(self, montant, article):
        if montant > self.budget:
            print(f'Budget insuffisant pour acheter : {article}')
        else:
            self.budget -= montant
            self.achat.append(article)

    def afficher_solde(self):
        print(f'Il vou reste {self.budget} € à dépenser')

    def convertir_en_dollard(self):
        dollars = self.budget * 1.08
        print(f'Il reste {round(dollars, 2)} $ à dépenser')
    
    def afficher_inventaire(self):
        print(f"vous avez {self.achat} dans votre inventaire")

class MarcheIA:
    def __init__(self, prix_service = {"GPU": 500, "Data": 200, "Coach": 100}):
        self.prix = prix_service

    def afficher_catalogue(self):
        print(f'vous pouvez acheter un GPU à {self.prix["GPU"]} €, un Data à {self.prix["Data"]} € ou un Coach à {self.prix["Coach"]} €')

    def retirer_du_stock(self, article):
        if article in self.prix:
            del self.prix[article]
            print(f"L'article {article} n'est plus disponible à l'achat")


mon_compte = CompteProjet(1000)
nvidia_store = MarcheIA()
article_a_vendre = list(nvidia_store.prix.keys())

for nom in article_a_vendre:
    prix = nvidia_store.prix[nom]
    mon_compte.depenser(prix, nom)
    if nom in mon_compte.achat:
        mon_compte.afficher_solde()
        mon_compte.afficher_inventaire()
        nvidia_store.retirer_du_stock(nom)
