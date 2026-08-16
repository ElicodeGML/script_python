class Sportif:
    def __init__(self, energie_initial = 100):
        self.activitees_faites = []
        self.energie = energie_initial

    def s_entrainer(self, cout_energie, nom_exo):
        if cout_energie > self.energie:
            print(f"trop fatigué pour faire des {nom_exo}")
        else:
             self.energie -= cout_energie
             self.activitees_faites.append(nom_exo)
             print(f"L'exo {nom_exo} réussi")
             print(f"energie restantes = {self.energie}")

class Salledesport:
    def __init__(self):
        self.catalogue = {
            "pompes": 20, 
            "Tractions": 30, 
            "Squats": 15
        }

    def supprimer_exo(self, nom_exo):
        if nom_exo in self.catalogue:
            del self.catalogue[nom_exo]
            print(f" --- {nom_exo} n'est plus disponnible ---")

mon_athlete = Sportif(100)
ma_salle = Salledesport()
liste_exo = list(ma_salle.catalogue.keys())

for nom in liste_exo:
    cout = ma_salle.catalogue[nom]
    mon_athlete.s_entrainer(cout, nom)
    if nom in mon_athlete.activitees_faites:
        ma_salle.supprimer_exo(nom)

print(f"Activitées terminées : {mon_athlete.activitees_faites}")
print(f"exo restant : {ma_salle.catalogue}")
