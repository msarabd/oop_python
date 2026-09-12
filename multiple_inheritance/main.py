class Team:

    def setTeam(self, team):
        self.team = team

    def getTeam(self):
        return self.team

class Tipe():

    def setTipe(self, tipe):
        self.tipe = tipe

    def getTipe(self):
        return self.tipe

class Player(Team,Tipe): # multiple inheritance = 1 subclass banyak super class

    def __init__(self, name, stamina):
        self.name = name
        self.stamina = stamina

Andi = Player("Andi", 100)
# tidak bisa pakai cara ini, karena atribut belum diinisiasi
# Andi.team = "Barcelona"
# Andi.tipe = "Kiper"

Andi.setTeam("Barcelona") # mengambil method class Team
Andi.setTipe("Kiper") # mengambil method class Kiper

print(Andi.getTeam())
print(Andi.getTipe())
print(Andi.__dict__)