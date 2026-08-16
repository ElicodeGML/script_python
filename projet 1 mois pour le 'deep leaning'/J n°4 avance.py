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

    def depenser(self, montant):
        if montant > self.budget:
            print('Budget insuffisant')
        else:
            self.budget -= montant
            print('Achat effectuer')

    def afficher_solde(self):
        print(f'Il vou reste {self.budget} € à dépenser')

    def convertir_en_dollard(self):
        dollars = self.budget * 1.08
        print(f'Il reste {round(dollars, 2)} $ à dépenser')

mon_ia = CompteProjet()
rappor = mon_ia.prix_dollars_depart()
mon_ia.ajouter_fonds(500)
rapport = mon_ia.afficher_solde()
rapports = mon_ia.convertir_en_dollard()
mon_ia.depenser(200)
rapport = mon_ia.afficher_solde()
rapports = mon_ia.convertir_en_dollard()
mon_ia.depenser(3000)
rapport = mon_ia.afficher_solde()
rapports = mon_ia.convertir_en_dollard()
