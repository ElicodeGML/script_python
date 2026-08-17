# === Classe pour représenter un athlète ===
class Sportif:
    """Gère l'énergie et les activités d'un sportif."""
    def __init__(self, energie_initial=100):
        """Initialise un sportif avec une énergie par défaut."""
        self.activitees_faites = []
        self.energie = energie_initial

    def s_entrainer(self, cout_energie, nom_exo):
        """Exécute un exercice si l'énergie est suffisante."""
        if cout_energie > self.energie:
            print(f"trop fatigué pour faire des {nom_exo}")
        else:
            self.energie -= cout_energie
            self.activitees_faites.append(nom_exo)
            print(f"L'exo {nom_exo} réussi")
            print(f"energie restantes = {self.energie}")


# === Classe pour représenter une salle de sport ===
class Salledesport:
    """Gère le catalogue des exercices disponibles."""
    def __init__(self):
        """Initialise une salle avec des exercices et leurs coûts énergétiques."""
        self.catalogue = {
            "pompes": 20,
            "Tractions": 30,
            "Squats": 15
        }

    def supprimer_exo(self, nom_exo):
        """Supprime un exercice du catalogue."""
        if nom_exo in self.catalogue:
            del self.catalogue[nom_exo]
            print(f" --- {nom_exo} n'est plus disponnible ---")


# === Programme principal ===
if __name__ == "__main__":
    # Créer une instance d'athlète et de salle de sport
    mon_athlete = Sportif(100)
    ma_salle = Salledesport()
    liste_exo = list(ma_salle.catalogue.keys())

    # Faire exécuter les exercices et les supprimer après réussite
    for nom in liste_exo:
        cout = ma_salle.catalogue[nom]
        mon_athlete.s_entrainer(cout, nom)
        if nom in mon_athlete.activitees_faites:
            ma_salle.supprimer_exo(nom)

    # Afficher les résultats
    print(f"Activitées terminées : {mon_athlete.activitees_faites}")
    print(f"exo restant : {ma_salle.catalogue}")
