class Karyawan:
    # class variable
    jumlah_karyawan = 0

    def __init__(self, inputName, inputUmur, inputGaji):
        self.name = inputName
        self.umur = inputUmur
        self.gaji = inputGaji
        Karyawan.jumlah_karyawan += 1

    # void fuction, method tanpa return, tanpa argumen
    def siapa(self):
        print("saya sebagai", self.name)

    # method dengan argumen, tanpa return
    def tambahGaji(self, tambah):
        self.gaji += tambah

    # method dengan return
    def getGaji(self):
        return self.gaji


karyawan1 = Karyawan("direktur", 65, 25000)

karyawan1.siapa()

print(karyawan1.gaji)
karyawan1.tambahGaji(10000)

print(karyawan1.getGaji())
