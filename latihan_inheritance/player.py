from abc import ABC, abstractmethod
import random

class Player(ABC):
    __jumlah = 0;

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
        if value >= 0:
            self.__stamina = value
        else:
            self.__stamina = 0

    @staticmethod
    def jumlah():
        return Player.__jumlah

    @abstractmethod
    def bermain(self):
        pass

class Kicker(Player):
    __jumlahGol = 0

    def __init__(self, name, shotStat, stamina=100):
        super().__init__(name, stamina)
        self.__shotStat = shotStat

    @property
    def shotStat(self):
        return self.__shotStat

    @shotStat.setter
    def shotStat(self, value):
        self.__shotStat = value

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
        print(f"{self.name} (penendang) siap bertanding!")

    def menendang(self, keeper):
        print(f'''{self.name} bersiap melakukan tembakan
3...
2...
1...
(jebret)
''')
        angka_random = random.randint(0, 1)
        if angka_random == 1:
            keeper.menangkap(self)
        else:
            print("Bola melambung jauh dari gawang saudara-saudara")
            self.stamina -= 0.2 * self.shotStat
            keeper.stamina -= 0.2 * keeper.catchStat
            
class Keeper(Player):
    __jumlahTepisan = 0

    def __init__(self, name, catchStat, stamina=100):
        super().__init__(name, stamina)
        self.__catchStat = catchStat

    @property
    def catchStat(self):
        return self.__catchStat

    @catchStat.setter
    def catchStat(self, value):
        self.__catchStat = value

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
        print(f"{self.name} (kiper) siap bertanding!")

    def menangkap(self, kicker):
        print(f"Bola mengarah ke arah gawang, {self.name} mencoba untuk menepis bola")

        peluangMasuk = kicker.shotStat / (kicker.shotStat + self.catchStat)
        if peluangMasuk > 0.5:
            print(f"Gol gol gol gol.... {kicker.name} berhasil memasukkan bola ke gawang")
            kicker.stamina -= 0.2 * kicker.shotStat
            self.stamina -= 0.3 * self.catchStat
            kicker.shotStat *= 4/5
            Kicker.setJumlahGol(Kicker.getJumlahGol() + 1)
            
        else:
            print(f"(Puk) {self.name} tidak disangka dapat menghalau tendangan yang begitu cepat")
            kicker.stamina -= 0.3 * kicker.shotStat
            self.stamina -= 0.2 * self.catchStat
            self.catchStat *= 3/5
            Keeper.setJumlahTepisan(Keeper.getJumlahTepisan() + 1)