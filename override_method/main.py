class Player:
    def __init__(self, name, marketVal):
        self.name = name
        self.marketVal = marketVal

    """  
    def getInfo(self, tipe):
        print("{} dengan tipe {} dihargai {} dolar amerika".format(self.name, tipe, self.marketVal))
    bisa begini tapi ini hanya mengambil method dari superclass dan perlu parameter tambahan, bukan override
    """

    # override
    def getInfo(self):
        print("ini adalah method superclass")
        print("{} dihargai {} dolar amerika".format(self.name, self.marketVal))
        
class Defender(Player):
    def __init__(self, name):
        super().__init__(name, 20000)

    """
    def getInfo(self):
        super().getInfo("Defender")
    ini pasangannya kalau hanya ingin mengambil method pada superclass nyapi
    """

    def getInfo(self):
        print("ini adalah method subclass")
        print("{} dengan tipe DEFENDER dihargai {} dolar amerika".format(self.name, self.marketVal))

class Forward(Player):
    def __init__(self, name):
        super().__init__(name, 20000)

bastoni = Defender("bastoni")
yamal = Forward("yamal")

bastoni.getInfo()  # ini pakai method subclass
print()
yamal.getInfo() # ini pakai method superclass