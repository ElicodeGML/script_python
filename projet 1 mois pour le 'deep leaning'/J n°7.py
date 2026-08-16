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
        print(f"""Score: {bot_a.name} à {bot_a.energie} energie
       {bot_degat.name} à {bot_degat.energie} energie
       {bot_soin.name} à {bot_soin.energie} energie
              """)

class RobotGuerrier(Robot):
    def __init__(self, nom, energie = 100):
        super().__init__(nom, energie)
        self.bouclier = 50

    def encaisser_degat(self, degat):
        if self.bouclier > 0:
            reduction = degat / 2
            self.energie -= reduction
            self.bouclier -= 10
            print(f"Bouclier actif il reste {self.energie} vie")
        else:
            self.degat = self.degat

class RobotSoigneur(Robot):
    def __init__(self, nom, energie = 100):
        self.name = nom
        self.energie = energie

    def soin(self, quantité_soin):
            self.energie += quantité_soin
            print(f"{self.name} se soigne de {quantité_soin} HP")

bot_a = Robot("Alpha")
bot_degat = RobotGuerrier("Guerrier-Z")
bot_soin = RobotSoigneur("Soin-1")

while bot_a.energie >= 0 and bot_degat.energie >= 0 and bot_soin.energie >= 0:
    bot_a.attaquer_bot(bot_degat)
    if bot_degat.energie > 0:
        bot_degat.attaquer_bot(bot_soin)
        if bot_soin.energie > 0:
            bot_soin.attaquer_bot(bot_a)
            bot_soin.soin(bot_soin.energie//2)
        print("-_" * 10)



if bot_a.energie <= 0:
    bot_a.energie = 0
    print(f"{bot_a.name} à perdue : {bot_a.energie}")
elif bot_soin.energie <= 0:
    bot_soin.energie = 0
    print(f"{bot_soin.name} à perdue : {bot_soin.energie}")
else:
    bot_degat.energie = 0
    print(f"{bot_degat.name} à perdue : {bot_degat.energie}")
