class Player:
    def __init__(self, name, marketVal):
        self.name = name
        self.marketVal = marketVal
        self.getInfo

    @property
    def getInfo(self):
        print("{} dihargai {} dolar amerika".format(self.name, self.marketVal))
        
class Defender(Player):
    def __init__(self, name):
        # Player.__init__(self, name, 20000) ini statis, jadi saat superclass nya diubah, class disini juga harus diubah, butuh parameter self
        super().__init__(name, 20000) # dinamis, saat superclass nya berubah tidak masalah, tidak perlu parameter self juga

class Forward(Player):
    def __init__(self, name):
        # Player.__init__(self, name, 50000)
        super().__init__(name, 20000)

# bastoni = Defender("bastoni", 200) ini salah karena pada subclassnya udah diperbarui dimana init nya hanya mengambil 1 parameter
bastoni = Defender("bastoni")
yamal = Forward("yamal")

print(bastoni.name)