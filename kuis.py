from abc import ABC, abstractmethod
import random

class Player(ABC):
    __jumlah = 0

    def __init__(self, name, stamina=100):
        self.__name = name
        self.__stamina = stamina
        Player.__jumlah += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        self.__stamina = max(0, value)

    @abstractmethod
    def bermain(self):
        pass


class Kicker(Player):
    __jumlahGol = 0

    def __init__(self, name, shotStat, stamina=100):
        super().__init__(name, stamina)
        self.__shotStat = shotStat
        self.bermain()

    @property
    def shotStat(self):
        return self.__shotStat

    @shotStat.setter
    def shotStat(self, value):
        self.__shotStat = value

    @staticmethod
    def getJumlahGol():
        return Kicker.__jumlahGol

    @staticmethod
    def setJumlahGol(value):
        Kicker.__jumlahGol = value

    def bermain(self):
        print(f"{self.name} (penendang) siap untuk bertanding")

    def menendang(self, keeper):
        print(f'''{self.name} bersiap melakukan tendangan....
        3
        2
        1
        (jebret!)
        ''')

        chance = random.uniform(0, 1)
        prob_gol = self.shotStat / (self.shotStat + keeper.catchStat)

        if chance < prob_gol:
            keeper.menangkap(self, berhasil=False)
        else:
            keeper.menangkap(self, berhasil=True)


class Keeper(Player):
    __jumlahTepisan = 0

    def __init__(self, name, catchStat, stamina=100):
        super().__init__(name, stamina)
        self.__catchStat = catchStat
        self.bermain()

    @property
    def catchStat(self):
        return self.__catchStat

    @catchStat.setter
    def catchStat(self, value):
        self.__catchStat = value

    @staticmethod
    def getJumlahTepisan():
        return Keeper.__jumlahTepisan

    @staticmethod
    def setJumlahTepisan(value):
        Keeper.__jumlahTepisan = value

    def bermain(self):
        print(f"{self.name} (kiper) siap untuk bertanding")

    def menangkap(self, kicker, berhasil=True):
        if not berhasil:
            print(f"gol gol gol gol... {kicker.name} berhasil mencetak gol!")
            Kicker.setJumlahGol(Kicker.getJumlahGol() + 1)
            self.stamina -= 0.3 * kicker.shotStat
            kicker.stamina -= 0.2 * self.catchStat
        else:
            print(f"(shiss) tidak disangka, {self.name} berhasil menepis bola!")
            Keeper.__jumlahTepisan += 1
            self.stamina -= 0.2 * kicker.shotStat
            kicker.stamina -= 0.3 * self.catchStat


player = input("Masukkan nama penendang: ")
stat = int(input("Masukkan nilai stat shooting (0 - 100) = "))
kicker1 = Kicker(player, stat)
player = input("Masukkan nama kiper: ")
stat = int(input("Masukkan nilai stat keeping (0 - 100) = "))
keeper1 = Keeper(player, stat)

while keeper1.stamina > 0 and kicker1.stamina > 0:
    kicker1.menendang(keeper1)

print("\n=== HASIL PERTANDINGAN ===")
print(f"Total gol: {Kicker.getJumlahGol()}")
print(f"Total tepisan: {Keeper.getJumlahTepisan()}")
print(f"Stamina terakhir {kicker1.name}: {kicker1.stamina}")
print(f"Stamina terakhir {keeper1.name}: {keeper1.stamina}")
