# magic method - method bawaan python

class Defender:

    # akan dieksekusi pertama kali saat instansiasi
    def __init__(self, name, stamina):
        self.name = name
        self.stamina = stamina
        print("objek anda berhasil dibuat")

    # akan dieksekusi saat kita memanggil objek itu sendiri, biasanya dipakai saat debug
    def __repr__(self):
        return "(debug) ini adalah repr"

    # sama seperti method, tetapi biasanya dipakai saat program sudah jadi
    def __str__(self):
        return "ini adalah str"

    # contoh method aritmatika, dieksekusi saat memanggil objek1 + objek2
    def __add__(self, objek):
        return self.stamina + objek.stamina
    
player1 = Defender("Andi", 88)
player2 = Defender("Budi", 100)
print(player1)
print(player1 + player2)