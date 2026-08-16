class CompteProjet:
    def prix_dollars_depart(self):
        dollar = self.budget * 1.08
        print(f'le budget initial est de {round(dollar, 2)} $')

    def __init__ (self, budget_initial = 1000):
        self.budget = budget_initial
        print(f'le budget initial est de {budget_initial} €. ')
        
    def ajouter_fonds(self, montant):
        self.budget += montant
        print(f"{montant} € ont été ajouter")

    def depenser(self, montant, article):
        if montant > self.budget:
            print(f'Budget insuffisant pour acheter : {article}')
        else:
            self.budget -= montant
            print(f'Achat  de {article} pour un prix de {montant} € à été effectué"')

    def afficher_solde(self):
        print(f'Il vou reste {self.budget} € à dépenser')

    def convertir_en_dollard(self):
        dollars = self.budget * 1.08
        print(f'Il reste {round(dollars, 2)} $ à dépenser')

class MarcheIA:
    def __init__(self, prix_service = {"GPU": 500, "Data": 200, "Coach": 100}):
        self.prix = prix_service

    def afficher_catalogue(self):
        print(f'vous pouvez acheter un GPU à {self.prix["GPU"]} €, un Data à {self.prix["Data"]} € ou un Coach à {self.prix["Coach"]} €')

mon_compte = CompteProjet(1000)
nvidia_store = MarcheIA()

nvidia_store.afficher_catalogue()
mon_compte.depenser(nvidia_store.prix["GPU"], "GPU")
mon_compte.afficher_solde()
