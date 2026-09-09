class Pekerja:
    # __jumlah_pekerja = 0 ini private variable bisa nempel di class juga
    # _jumlah_pekerja = 0 ini protected variable bisa nempel di class juga

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # private instance variable
        self.__salary = "private" # tidak bisa diakses (dilihat nilainya) ataupun di perbarui nilainya di luar class
        # protected instance variable
        self._rumah = "private" # sama aja seperti public variable, tetapi memberikan label protected dimana kita sebagai dev tidak boleh mengubah


budi = Pekerja("budi", 23)

print(budi.__dict__)
# print(budi.__private) akan error karena private variable tidak bisa dilihat nilainya
# budi.__private = "ada" ini tidak akan menginisialisasi private variable yang udah ada, melainkan membuat atau menambah variable baru pada object

budi._rumah = "talangsari" # akan mengubah nilai dari protected variable, dimana ini menyalahi aturan protected variable
print(budi.__dict__)





