# Copied and normalized Python script from scripts_/Revision class.py
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


nb_1 = Calculatrice("score 1", x)

print(f"{x} plus {y} égal {nb_1.additionner_score()}")
print(f"{a} moins {b} égal {nb_1.soustraire_score()}")
print(f"{c} fois {d} égal {nb_1.multiplier_score()}")
print(f"{e} diviser {f} égal {round(nb_1.diviser_score(), 2)}")
