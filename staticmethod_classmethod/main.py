class Pekerja:

    # private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Pekerja.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Pekerja.__jumlah

    # method ini hanya berlaku untuk class
    def getJumlah1():
        return Pekerja.__jumlah

    # method static (decorator = @) nempel ke class dan objek
    @staticmethod
    def getJumlah2(): # tanpa argumen
        return Pekerja.__jumlah # kalau nama class nya diubah, ini harus diubah juga

    @classmethod
    def getJumlah3(cls): # ga harus pakai self
        return cls.__jumlah # dengan argumen, dimana cls ini bisa diisi class ataupun objek


andi = Pekerja("andi")
print(andi.getJumlah())
budi = Pekerja("budi")
cantikan = Pekerja("cantika")

print(Pekerja.getJumlah1())
print(Pekerja.getJumlah2())
print(budi.getJumlah2())
print(Pekerja.getJumlah3())
print(budi.getJumlah3())


