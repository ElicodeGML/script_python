class Robot:
    def __init__(self, nom, energie = 100):
        self.name = nom
        self.energie = energie

    def se_presenter(self):
        print(f"Bonjour je m'appelle {self.name}")
    
    def attaquer_bot(self, cible = 100):
        cible
        if self.energie < 0:
            self.energie = 0
        else:
            if self.energie >= 20:
                self.energie - 20
                print(f"vous avez dépenser 20 energie")
                print(f"Il vous reste {self.energie} energie")
                cible.energie -= 20
            else:
                print(f"Vous n'avez pas assez d'energie")

bot_a = Robot("Beta")
bot_b = Robot("Alpha")

while bot_a.energie >= 0 and bot_b.energie >= 0:
    bot_a.attaquer_bot(bot_b)
    if bot_b.energie > 0:
        bot_b.attaquer_bot(bot_a)
        print(f"""Score: {bot_a.name} à {bot_a.energie} energie
                         {bot_b.name} à {bot_b.energie} energie
              """)
        print("-" * 20)

if bot_a.energie <= 0:
    print(f"{bot_a.name} à gagné")
else:
    print(f"{bot_b.name} à gagné")