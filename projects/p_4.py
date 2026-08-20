# ============================================================================
# GESTION DE COMPTE PROJET - Deep Learning
# ============================================================================

class CompteProjet:
    """Classe pour gérer le budget et les achats d'un projet IA."""
    
    def __init__(self, budget_initial=1000, p_achats=None):
        """Initialise le compte avec un budget initial et une liste d'achats."""
        self.budget = budget_initial
        self.achat = p_achats if p_achats is not None else []
        print(f'le budget initial est de {budget_initial} €. ')

    # Méthodes de consultation du budget
    def afficher_solde(self):
        """Affiche le budget restant en euros."""
        print(f'Il vou reste {self.budget} € à dépenser')

    def prix_dollars_depart(self):
        """Convertit le budget initial en dollars."""
        dollar = self.budget * 1.08
        print(f'le budget initial est de {round(dollar, 2)} $')

    def convertir_en_dollard(self):
        """Convertit le budget restant en dollars."""
        dollars = self.budget * 1.08
        print(f'Il reste {round(dollars, 2)} $ à dépenser')

    # Méthodes de gestion du budget
    def ajouter_fonds(self, montant):
        """Ajoute des fonds au budget."""
        self.budget += montant
        print(f"{montant} € ont été ajouter")

    def depenser(self, montant, article):
        """Dépense une somme pour acheter un article si le budget le permet."""
        if montant > self.budget:
            print(f'Budget insuffisant pour acheter : {article}')
        else:
            self.budget -= montant
            self.achat.append(article)

    # Méthodes d'inventaire
    def afficher_inventaire(self):
        """Affiche la liste des articles achetés."""
        print(f"vous avez {self.achat} dans votre inventaire")


class MarcheIA:
    """Classe pour gérer le marché et les services IA disponibles."""
    
    def __init__(self, prix_service=None):
        """Initialise le marché avec les prix des services."""
        if prix_service is None:
            prix_service = {"GPU": 500, "Data": 200, "Coach": 100}
        self.prix = prix_service

    def afficher_catalogue(self):
        """Affiche tous les services disponibles et leurs prix."""
        print(f'vous pouvez acheter un GPU à {self.prix["GPU"]} €, un Data à {self.prix["Data"]} € ou un Coach à {self.prix["Coach"]} €')

    def retirer_du_stock(self, article):
        """Retire un article du stock une fois acheté."""
        if article in self.prix:
            del self.prix[article]
            print(f"L'article {article} n'est plus disponible à l'achat")


# ============================================================================
# PROGRAMME PRINCIPAL
# ============================================================================

# Initialisation
mon_compte = CompteProjet(1000)
nvidia_store = MarcheIA()
article_a_vendre = list(nvidia_store.prix.keys())

# Boucle d'achat
for nom in article_a_vendre:
    prix = nvidia_store.prix[nom]
    mon_compte.depenser(prix, nom)
    if nom in mon_compte.achat:
        mon_compte.afficher_solde()
        mon_compte.afficher_inventaire()
        nvidia_store.retirer_du_stock(nom)
