class Pemain:
    __jumlahPemain = 0
    
    def __init__(self, nama, klub, stamina = 100):
        self.__nama = nama
        self.__klub = klub
        self.__stamina = stamina
        self.__jumlahPemain += 1
        self.bermain()

    def tampilkan_profil(self):
        print("Pemain: {} | Klub: {} | Stamina: {}".format(self.nama, self.klub, self.stamina))

    def bermain(self):
        self.__stamina -= 10
        print(f"{self.__nama} bermain di lapangan.")

    @classmethod
    def getJumlah(cls):
        return cls.__jumlahPemain

class Penyerang(Pemain):

    def __init__(self, nama, klub, stamina = 100, jumlah_gol = 0):
        super().__init__(nama, klub, stamina)
        self.jumlah_gol = jumlah_gol

    def bermain(self):
        super().bermain()
        print(f"{self.nama} fokus menyerang pertahanan lawan.")

    # def cetak_gol(self):
    #     self.jumlah_gol += 1
    #     print("GOOOL! {} mencetak angka. Total gol: {}".format(self.nama, self.jumlah_gol))

class Bek(Pemain):

    def __init__(self, nama, klub, stamina = 100, jumlah_tekel = 0):
        super().__init__(nama, klub, stamina)
        self.jumlah_tekel = jumlah_tekel

    def tampilkan_profil(self):
        print("BEK TANGGUH -> Nama: {} | Klub: {} | Tekel Sukses: {}".format(self.nama, self.klub, self.jumlah_tekel))

    def lakukan_tekel(self):
        self.jumlah_tekel += 1
        self.stamina -= 5
        print("{} melakukan tekel bersih! Stamina tersisa: {}".format(self.nama, self.stamina))

striker = Penyerang("Mbappe", "Real Madrid")
defender = Bek("Van Dijk", "Liverpool")

striker.tampilkan_profil()
striker.bermain()
striker.cetak_gol()
striker.cetak_gol()

print("-" * 20)

defender.tampilkan_profil()
defender.lakukan_tekel()
defender.bermain()
defender.tampilkan_profil()