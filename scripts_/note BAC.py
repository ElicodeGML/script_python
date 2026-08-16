moyenne_oui = float(input("quel est ta note du BAC ?"))

if 12 <= moyenne_oui > 14:
    print("Tu as la mention assez bien.")
elif 14 <= moyenne_oui > 16:
    print("Tu as la mention bien.")
elif 16 <= moyenne_oui > 18:
    print("Tu as la mention très bien")
elif moyenne_oui >= 18:
    print("Tu as les felicitations du jury")
else:
    print("Tu n'as pas de mention")