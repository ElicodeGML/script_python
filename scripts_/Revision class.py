# class Perso:
#     def __init__(self, name, th_name, age):
#         self.name = name
#         self.th_name = th_name
#         self.age = age
#         self.xp = 0

#     def augmenter_xp(self, exp):
#         self.xp += exp
#         print(f"    {self.th_name} a gagné(e) {exp} experience")

#     def info(self):
#         print(f"Perso : {self.name} {self.th_name} a {self.age} ans et a {self.xp} experience")

#  # perso n°1
# dante = Perso("Dante", "Jhon", 20)
# dante.info()

#  # perso n°2
# emily = Perso("Saki", "Emily", 46)
# emily.augmenter_xp(2)
# emily.info()

import random

x = random.randint(1, 50)
y = random.randint(1, 50)
a = random.randint(1, 50)
b = random.randint(1, 50)
c = random.randint(1, 50)
d = random.randint(1, 50)
e = random.randint(1, 50)
f = random.randint(1, 50)

class Calculatrice:
    def __init__(self, name, score_1 = x, score_2 = y):
        self.name = name
        self.score = score_1
        self.scores = score_2
        self.resultat = 0

    def additionner_score(self):
        self.resultat = self.score + self.scores
        return (self.resultat)

    def soustraire_score(self):
        if a > b:
            self.resultat = self.score - self.scores
            return(self.resultat)
        else:
            self.resultat = self.score - self.scores
            return(f"""{a} moins {b} est negatif.
{a} moins {b} égal 0 moins {b - a}""")

    def multiplier_score(self):
        self.resultat = self.score * self.scores
        return(self.resultat)

    def diviser_score(self):
        self.resultat = self.score / self.scores
        return(self.resultat)

    # def carre_score(self):
    #     self.score ** 2
    #     return(x * x)
    
    # def racine_carre_score(self):
    #     self.score // 2
    #     return(x / x)

nb_1 = Calculatrice("score 1", x)

print(f"{x} plus {y} égal {nb_1.additionner_score()}")
print(f"{a} moins {b} égal {nb_1.soustraire_score()}")
print(f"{c} fois {d} égal {nb_1.multiplier_score()}")
print(f"{e} diviser {f} égal {round(nb_1.diviser_score(), 2)}")


# print(f"{x} au carré égal {nb_1.carre_score}")
# print(f"la racine carré de {x} égal {nb_1.racine_carre_score}")
# print(f"{y} au carré égal {nb_2.carre_score}")
# print(f"la racine carré de {y} égal {nb_2.racine_carre_score}")
