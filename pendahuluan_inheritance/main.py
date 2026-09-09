class Player: # superclass

    def __init__(self, name, marketVal):
        self.name = name
        self.marketVal = marketVal

class Defender(Player): # subclass
    pass


andi = Player("andi", 10000)
budi = Defender("budi", 20000)
print(andi.name)
print(help(Defender))