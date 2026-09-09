class Pekerja:
    # class variable
    jumlah_pekerja = 0

    def __init__(self, nama, umur, gaji, potongGaji, tunjangan):
        self.nama = nama # nilai nama ini nyambung sama yang atas, argumennya (tidak masalah namanya sama dengan atributnya)
        self.umur = umur
        self.gaji = gaji
        self.potongGaji = potongGaji
        self.tunjangan = tunjangan
        Pekerja.jumlah_pekerja += 1

    def blunder(self, atasan):
        print(self.nama, "melakukan blunder")
        atasan.marah(self)

    def marah(self, atasan):
        print(self.nama, "memarahi", atasan.nama)
        atasan.dimarahi(self, self.potongGaji)

    def dimarahi(self, atasan, potongGaji):
        print(self.nama, "dimarahi", atasan.nama)
        besar_potongan = potongGaji - self.tunjangan
        print(self.nama, "dipotong gajinya sebesar:", besar_potongan)
        self.gaji -= besar_potongan
        print("gaji akhir yang akan didapatkan", self.nama, ":", self.gaji)

direktur = Pekerja("direktur", 65, 100000, 10000, 20000)
andi = Pekerja("andi", 34, 25000, 10000, 2000)

andi.blunder(direktur)
print("\n")
andi.blunder(direktur)
print("\n")
direktur.blunder(andi)

