membre = [
    {"nom": "Marc", "age": 24},
    {"nom": "Leo", "age": 18},
    {"nom": "Colin", "age": 38},
    {"nom": "Ruben", "age": 2},
    {"nom": "Eliot", "age": -3}
]

def cat(un_membre):
        if un_membre["age"] >= 18:
            return("un Adult")
        elif un_membre["age"] >= 120 or un_membre["age"] <= 0:
             return("une Erreur d'age")
        else:
            return("un Enfant")

for i in membre:
    decision = cat(i)
    print(f"{i["nom"]} à {i["age"]} ans c'est {decision}")
    